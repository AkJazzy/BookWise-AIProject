import os
from dotenv import load_dotenv

def load_env():
    load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
CHROMA_DB_DIR = os.getenv("CHROMA_DB_DIR", "vector_db")