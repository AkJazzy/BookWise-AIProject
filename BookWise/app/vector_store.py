import chromadb
from chromadb.config import Settings
from app.embeddings import embed_text
from app.config import CHROMA_DB_DIR

client = chromadb.Client(Settings(chroma_db_impl="duckdb+parquet", persist_directory=CHROMA_DB_DIR))
collection = client.get_or_create_collection("books")

def add_documents(docs, ids):
    embeddings = [embed_text(d) for d in docs]
    collection.add(documents=docs, embeddings=embeddings, ids=ids)

def query_vector_db(query, top_k=5):
    embedding = embed_text(query)
    results = collection.query(query_embeddings=[embedding], n_results=top_k)
    return results