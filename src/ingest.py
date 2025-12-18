from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
from typing import List

def load_data(data_path: str) -> List[Document]:
    loader = DirectoryLoader(
        path=data_path,
        glob="*.pdf",
        loader_cls=PyPDFLoader,
        show_progress=False
    )
    documents = loader.load()
    return documents

def filter_metadata(doc: List[Document]) -> List[Document]:
    filtered_doc = []
    for d in doc:
        src = d.metadata.get("source")
        filtered_doc.append(Document(
            page_content=d.page_content,
            metadata={"source": src}
        ))
    return filtered_doc

def text_split(documents: List[Document]) -> List[Document]:
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=100
    )
    chunk = text_splitter.split_documents(documents)
    return chunk

def build_chunks(data_path: str = "data") -> List[Document]:
    doc = load_data(data_path)
    new_doc = filter_metadata(doc)
    chunks = text_split(new_doc)
    return chunks
