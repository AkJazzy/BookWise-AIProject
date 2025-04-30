# 📚 BookWise – Ask Your Books AI

BookWise is an AI-powered application that allows you to upload books in `.txt`, `.pdf`, or image formats (`.jpg`, `.png`) and ask natural language questions. Whether you're studying, researching, or reviewing, BookWise helps you retrieve smart, summarized answers instantly.

---

## 🚀 Features

- ✅ Upload books in TXT, PDF, or image formats
- 🔎 Extract text using Tesseract OCR & PDFPlumber
- 🧠 Semantic search powered by SentenceTransformers & ChromaDB
- 💬 Summarization and Q&A using Google Gemini API
- 🧾 Chapter detection for structure-aware answering
- 🗂️ Session memory to track your past queries
- 🌙 Modern dark-themed Streamlit UI

---

## 🛠 Tech Stack

- **Frontend**: Streamlit
- **Backend**: Flask
- **Vector DB**: ChromaDB
- **LLM**: Google Gemini
- **Text Extraction**: Tesseract OCR, PDFPlumber
- **Embeddings**: SentenceTransformers

---

## 🖼 Architecture

![Architecture Diagram](BookWise_Architecture_with_Logo.png)

---

## 🧪 Getting Started

```bash
git clone https://github.com/yourusername/BookWise.git
cd BookWise
pip install -r requirements.txt
```

1. Add your Google Gemini API key to `.env`
2. Run the app:

```bash
streamlit run ui/streamlit_app.py
```

---

## 📄 Documentation

- [📘 Full PDF Documentation](./BookWise_Documentation_Final_With_Logo_Architecture.pdf)

---

## 📬 Contact

For queries or collaborations, feel free to reach out at [your-email@example.com].

---

> BookWise brings intelligent Q&A to your personal library. Just upload, ask, and learn.
