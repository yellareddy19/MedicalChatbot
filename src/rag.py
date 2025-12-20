from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.history_aware_retriever import create_history_aware_retriever


def build_rag_chain(retriever):
    llm = ChatOpenAI(model="gpt-4o", temperature=0)

    # 1) Make retriever aware of history (so follow-up questions work)
    contextualize_prompt = ChatPromptTemplate.from_messages([
        ("system",
         "You are given a chat history and the latest user question. "
         "Rewrite the user question into a standalone question that includes any needed context. "
         "Do NOT answer. Only rewrite."),
        MessagesPlaceholder("chat_history"),
        ("human", "{input}")
    ])

    history_aware_retriever = create_history_aware_retriever(
        llm=llm,
        retriever=retriever,
        prompt=contextualize_prompt
    )

    # 2) Answer prompt uses context + chat history
    system_prompt = (
        "You are a helpful medical assistant. "
        "Use the following context to answer the question.\n\n"
        "Context:\n{context}\n\n"
        "If the answer is not in the context, say you are not sure."
    )

    answer_prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        MessagesPlaceholder("chat_history"),
        ("human", "{input}")
    ])

    qa_chain = create_stuff_documents_chain(
        llm=llm,
        prompt=answer_prompt,
        document_variable_name="context"
    )

    rag_chain = create_retrieval_chain(history_aware_retriever, qa_chain)
    return rag_chain
