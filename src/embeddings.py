from dotenv import load_dotenv
import os
from langchain_openai import OpenAIEmbeddings

def get_embeddings():
    load_dotenv()
    key = os.getenv("OPENAI_API_KEY")
    if not key:
        raise ValueError("OPENAI_API_KEY not set in .env")

    os.environ["OPENAI_API_KEY"] = key

    embeddings = OpenAIEmbeddings(
        model="text-embedding-3-small"
    )
    return embeddings
