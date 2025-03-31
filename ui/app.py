import streamlit as st
import pandas as pd
import os
import chromadb
import openai
from sentence_transformers import SentenceTransformer

st.title("Contract Search & Classification using ChromaDB")

# Configuration
USE_OPENAI = os.getenv("USE_OPENAI", "true").lower() == "true"
if not USE_OPENAI:
    local_model = SentenceTransformer("all-MiniLM-L6-v2")

# Initialize ChromaDB
chroma_client = chromadb.PersistentClient(path="./chroma_db")
collection = chroma_client.get_collection(name="contracts")

# Upload contract for search
uploaded_file = st.file_uploader("Upload contract to find similar ones", type=["txt", "pdf"])
contract_type = st.selectbox("Filter by contract type", ["", "NDA", "Employment Agreement", "Vendor Contract", "Lease Agreement", "M&A Contract"])

if uploaded_file is not None:
    text = uploaded_file.read().decode("utf-8")
    
    # Get embedding
    if USE_OPENAI:
        response = openai.Embedding.create(input=[text], model="text-embedding-ada-002")
        query_embedding = response["data"][0]["embedding"]
    else:
        query_embedding = local_model.encode(text)
    
    filters = {"type": contract_type} if contract_type else None
    results = collection.query(query_embeddings=[query_embedding], n_results=5, where=filters)
    df = pd.DataFrame(results["documents"][0], columns=["content"])
    st.write(df)
