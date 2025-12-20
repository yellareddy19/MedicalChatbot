from .ingest import build_chunks
from .embeddings import get_embeddings
from .pinecone_db import get_pinecone_client, ensure_index, get_vectorstore
from .rag import build_rag_chain

from langchain_core.messages import HumanMessage, AIMessage

# Simple in-memory store:
# { "session_id": [HumanMessage(...), AIMessage(...), ...] }
_SESSION_STORE = {}


def _get_history(session_id: str):
    if session_id not in _SESSION_STORE:
        _SESSION_STORE[session_id] = []
    return _SESSION_STORE[session_id]


class MedicalChatbotService:
    def __init__(self, data_path="data", index_name="medicalchatbot", namespace="medical_book_v1"):
        self.data_path = data_path
        self.index_name = index_name
        self.namespace = namespace

        self.vectorstore = None
        self.retriever = None
        self.rag_chain = None

    def _namespace_has_vectors(self, index) -> bool:
        stats = index.describe_index_stats()
        namespaces = stats.get("namespaces", {})
        ns = namespaces.get(self.namespace, {})
        return ns.get("vector_count", 0) > 0

    def setup(self):
        # 1) chunks (same as your notebook)
        chunks = build_chunks(self.data_path)

        # 2) embeddings
        embeddings = get_embeddings()
        dim = len(embeddings.embed_query("Medical chatbot"))  # sanity check / dimension

        # 3) pinecone index
        pc = get_pinecone_client()
        index = ensure_index(pc, self.index_name, dimension=dim)

        # 4) vectorstore with namespace (IMPORTANT)
        self.vectorstore = get_vectorstore(
            embeddings=embeddings,
            index_name=self.index_name,
            namespace=self.namespace
        )

        # 5) ingest only if namespace is empty
        if self._namespace_has_vectors(index):
            print(f"✅ Namespace '{self.namespace}' already has vectors. Skipping ingestion.")
        else:
            print(f"⬆️ Ingesting {len(chunks)} chunks into namespace '{self.namespace}'...")
            batch_size = 25  # free tier safe
            for i in range(0, len(chunks), batch_size):
                batch = chunks[i:i + batch_size]
                self.vectorstore.add_documents(batch)
                if i % (batch_size * 20) == 0:
                    print(f"Uploaded {i}/{len(chunks)} chunks...")

            print("✅ Ingestion completed.")

        # 6) retriever + rag chain
        self.retriever = self.vectorstore.as_retriever(
            search_type="similarity",
            search_kwargs={"k": 3}
        )

        # IMPORTANT: rag chain must support chat_history input
        self.rag_chain = build_rag_chain(self.retriever)

    def ask(self, question: str, session_id: str = "default") -> str:
        if not self.rag_chain:
            raise RuntimeError("Service not initialized. Call setup() first.")

        history = _get_history(session_id)

        response = self.rag_chain.invoke({
            "input": question,
            "chat_history": history
        })

        answer = response.get("answer", "")

        # Update history
        history.append(HumanMessage(content=question))
        history.append(AIMessage(content=answer))

        # Keep last N turns to control token usage
        MAX_TURNS = 6  # adjust as you like
        if len(history) > MAX_TURNS * 2:
            _SESSION_STORE[session_id] = history[-MAX_TURNS * 2:]

        return answer
