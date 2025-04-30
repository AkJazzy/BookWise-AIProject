from app.vector_store import query_vector_db
from app.gemini_llm import generate_summary

def answer_query(user_query):
    results = query_vector_db(user_query, top_k=5)
    docs = results["documents"][0]
    combined_context = "\n\n".join(docs)
    summary = generate_summary(combined_context, user_query)
    return summary