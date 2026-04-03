from langchain_google_genai import GoogleGenerativeAIEmbeddings
from src.config import EMBEDDING_MODEL

def create_embeddings():
    embeddings = GoogleGenerativeAIEmbeddings(model=EMBEDDING_MODEL)
    return embeddings
