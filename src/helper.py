from langchain_community.document_loaders import DirectoryLoader,PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
from typing import List

def load_data(data_path:str)-> List[Document]:
    loader=DirectoryLoader(
        from typing import List
        import os

        from langchain.schema import Document

        try:
            # prefer community loaders if available
            from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
        except Exception:
            try:
                from langchain.document_loaders import DirectoryLoader, PyPDFLoader
            except Exception:
                DirectoryLoader = None
                PyPDFLoader = None

        try:
            from langchain.text_splitter import RecursiveCharacterTextSplitter
        except Exception:
            RecursiveCharacterTextSplitter = None


        def load_pdfs(data_path: str) -> List[Document]:
            """Load PDF documents from `data_path` using a DirectoryLoader.

            Returns an empty list if the loader isn't available.
            """
            if DirectoryLoader is None or PyPDFLoader is None:
                return []
            loader = DirectoryLoader(path=data_path, glob="*.pdf", loader_cls=PyPDFLoader, show_progress=False)
            return loader.load()


        def filter_metadata(documents: List[Document]) -> List[Document]:
            """Return documents with reduced metadata (only `source`)."""
            filtered: List[Document] = []
            for doc in documents:
                src = getattr(doc, "metadata", {}).get("source")
                filtered.append(Document(page_content=doc.page_content, metadata={"source": src}))
            return filtered


        def text_split(documents: List[Document], chunk_size: int = 800, chunk_overlap: int = 100) -> List[Document]:
            """Split documents into chunks using RecursiveCharacterTextSplitter.

            Returns the original documents if the splitter isn't available.
            """
            if RecursiveCharacterTextSplitter is None:
                return documents
            splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
            return splitter.split_documents(documents)
