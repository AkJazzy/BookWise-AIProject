import google.generativeai as genai
from app.config import GOOGLE_API_KEY

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel("gemini-pro")

def generate_summary(context, query):
    prompt = f"""
    You are an AI reading assistant.

    Context:
    {context}

    Query:
    {query}

    Provide a clear and helpful answer.
    """
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"[Error generating summary: {e}]"