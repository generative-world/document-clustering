from fastapi import FastAPI, UploadFile, File
import openai
import numpy as np
import chromadb
import pickle
import os
from sentence_transformers import SentenceTransformer
from chromadb.utils.embedding_functions import OpenAIEmbeddingFunction
from sklearn.neighbors import KNeighborsClassifier

app = FastAPI()

# Configuration: Use OpenAI or Local Model
USE_OPENAI = os.getenv("USE_OPENAI", "true").lower() == "true"
if not USE_OPENAI:
    local_model = SentenceTransformer("all-MiniLM-L6-v2")

# Initialize ChromaDB
chroma_client = chromadb.PersistentClient(path="./chroma_db")
collection = chroma_client.get_or_create_collection(
    name="contracts",
    embedding_function=OpenAIEmbeddingFunction(api_key="your-openai-api-key") if USE_OPENAI else None
)

# Load contract classifier
with open("./models/classifier.pkl", "rb") as f:
    classifier = pickle.load(f)

@app.post("/classify/")
async def classify_contract(file: UploadFile = File(...)):
    text = await file.read()
    embedding = get_embedding(text.decode("utf-8"))
    
    # Predict contract type
    contract_type = classifier.predict([embedding.tolist()])[0]
    
    # Save contract with vector embedding
    collection.add(documents=[text.decode("utf-8")], embeddings=[embedding.tolist()], metadatas=[{"type": contract_type}])
    
    return {"message": "Contract stored successfully", "contract_type": contract_type}

@app.post("/search/")
async def search_contract(file: UploadFile = File(...), contract_type: str = None):
    text = await file.read()
    query_embedding = get_embedding(text.decode("utf-8"))
    
    # Find similar contracts with optional filtering by type
    filters = {"type": contract_type} if contract_type else None
    results = collection.query(query_embeddings=[query_embedding.tolist()], n_results=5, where=filters)
    return {"matches": results}

def get_embedding(text):
    if USE_OPENAI:
        response = openai.Embedding.create(input=[text], model="text-embedding-ada-002")
        return np.array(response["data"][0]["embedding"])
    else:
        return local_model.encode(text)
