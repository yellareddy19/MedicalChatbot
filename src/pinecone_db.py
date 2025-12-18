from dotenv import load_dotenv
import os
from pinecone import Pinecone, ServerlessSpec
from langchain_pinecone import PineconeVectorStore

def get_pinecone_client():
    load_dotenv()
    pinecone_key = os.getenv("PINECONE_API_KEY")
    if not pinecone_key:
        raise ValueError("PINECONE_API_KEY not set in .env")
    return Pinecone(api_key=pinecone_key)

def ensure_index(pc, index_name: str, dimension: int = 1536):
    # dimension must match embedding model (1536 for text-embedding-3-small)
    if not pc.has_index(index_name):
        pc.create_index(
            name=index_name,
            metric="cosine",
            dimension=dimension,
            spec=ServerlessSpec(cloud="aws", region="us-east-1")
        )
    return pc.Index(index_name)

def get_vectorstore(embeddings, index_name: str, namespace: str):
    return PineconeVectorStore(
        embedding=embeddings,
        index_name=index_name,
        namespace=namespace
    )
