from langchain_openai import ChatOpenAI
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate

def build_rag_chain(retriever):
    llm = ChatOpenAI(model="gpt-4o")

    system_prompt = (
        "You are a helpful medical assistant. give answers in short and concise manner. "
        "Use the following context to answer the question.\n\n"
        "{context}"
    )

    template = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("human", "{input}")
    ])

    qa_chain = create_stuff_documents_chain(
        llm,
        template,
        document_variable_name="context"
    )

    rag_chain = create_retrieval_chain(retriever, qa_chain)
    return rag_chain
