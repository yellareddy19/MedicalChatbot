from langchain_community.document_loaders import DirectoryLoader,PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
from typing import List

def load_data(data_path:str)-> List[Document]:
    loader=DirectoryLoader(
        path=data_path,
        glob="*.pdf",
        loader_cls=PyPDFLoader,
        show_progress=False

    )

def filter_metadata(doc:List[Document])->List[Document]:

    for doc in doc:
        src=doc.metadata.get("source")
        filtered_doc.append(Document(
            page_content=doc.page_content,
            metadata={
                "source":src
            }
        ))
    return filtered_doc

### now chunk the data

def text_split(documents:List[Document])->List[Document]:
    text_splitter=RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=100
    )
    chunk=text_splitter.split_documents(documents)
    return chunk
