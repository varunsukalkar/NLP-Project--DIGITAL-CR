# ----------------- Streamlit Imports -----------------
import streamlit as st  # 👈 Streamlit for UI

# ----------------- LangChain + Other Imports -----------------
import os
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEmbeddings, ChatHuggingFace, HuggingFaceEndpoint
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA


# ----------------- Load API Key -----------------
load_dotenv()
api_key = os.getenv("HUGGINGFACEHUB_API_TOKEN")

if not api_key:
    st.error("⚠️ Hugging Face API key not found. Please set it in your .env file.")
    st.stop()


# ----------------- Streamlit UI Setup -----------------
st.set_page_config(page_title="College Chatbot", layout="centered")
st.title("🎓 College Info Chatbot")
st.markdown("Ask anything related to your college. Type your question below 👇")

# ----------------- Load Documents (Fixed File Path) -----------------
file_path = r"E:\nlp data.pdf"  # 👈 Change path if needed
if not os.path.exists(file_path):
    st.error(f"❌ File not found: {file_path}")
    st.stop()

loader = PyPDFLoader(file_path)
documents = loader.load()

splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
docs = splitter.split_documents(documents)

if len(docs) == 0:
    st.warning("⚠️ No text found in the document. Please check your file.")
    st.stop()

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
db = FAISS.from_documents(docs, embeddings)

llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.3",
    task="text-generation",
    huggingfacehub_api_token=api_key
)
model = ChatHuggingFace(llm=llm)

qa = RetrievalQA.from_chain_type(llm=model, retriever=db.as_retriever())

# ----------------- Chat Section -----------------
user_input = st.text_input("💬 Ask your question:", key="input_box")

if st.button("Send"):
    if user_input.strip() == "":
        st.warning("Please enter a question.")
    else:
        with st.spinner("🤖 Thinking..."):
            try:
                result = qa.invoke(user_input)
                st.markdown(f"*Answer:* {result['result']}")
            except Exception as e:
                st.error(f"Error: {e}")

st.markdown("---")
st.caption("Built with Streamlit + LangChain + Hugging Face")