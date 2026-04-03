from langchain_core.vectorstores import InMemoryVectorStore
from src.embeddings import create_embeddings

def create_vector_store():
    embeddings=create_embeddings()
    vector_store = InMemoryVectorStore(embeddings)
    return vector_store

def store_docs(docs):
    vector_store=create_vector_store()
    document_ids = vector_store.add_documents(documents=docs)
    print(document_ids[:3])
    return vector_store

