import pickle
from sentence_transformers import SentenceTransformer

def train_embedding_model():
    """Train and save embeddings for contracts."""
    model = SentenceTransformer("all-MiniLM-L6-v2")
    with open("data/preprocessed_contracts.json", "r") as f:
        contracts = json.load(f)
    embeddings = model.encode(contracts)
    with open("models/embeddings.pkl", "wb") as f:
        pickle.dump(embeddings, f)

if __name__ == "__main__":
    train_embedding_model()
