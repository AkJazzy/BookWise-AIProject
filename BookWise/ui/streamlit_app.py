import streamlit as st
from app.utils import extract_text_from_image, extract_text_from_pdf, load_txt
from app.vector_store import add_documents
from app.retriever import answer_query
import uuid

st.set_page_config(page_title="📚 BookWise", layout="centered")
st.title("📚 BookWise – Ask Your Books AI")

# Initialize session memory
if "qa_history" not in st.session_state:
    st.session_state.qa_history = []

# Clear chat button
if st.button("🗑️ Clear Chat"):
    st.session_state.qa_history = []
    st.success("Chat history cleared!")

# Upload book (PDF, image, or TXT)
uploaded_file = st.file_uploader("Upload a book or page", type=["pdf", "txt", "png", "jpg", "jpeg"])
if uploaded_file:
    if uploaded_file.type == "application/pdf":
        content = extract_text_from_pdf(uploaded_file)
    elif uploaded_file.type.startswith("image/"):
        content = extract_text_from_image(uploaded_file)
    else:
        content = load_txt(uploaded_file)

    if content:
        doc_id = str(uuid.uuid4())
        add_documents([content], [doc_id])
        st.success("Book content indexed successfully!")

# Ask a question
query = st.text_input("Ask something about your book:")
if st.button("Ask") and query:
    answer = answer_query(query)
    st.session_state.qa_history.append((query, answer))

# Display chat history
for q, a in st.session_state.qa_history:
    st.markdown(f"**Q:** {q}")
    st.markdown(f"**A:** {a}")