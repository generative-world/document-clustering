import chromadb

def setup_chromadb():
    """Initialize ChromaDB."""
    chroma_client = chromadb.PersistentClient(path="./chroma_db")
    collection = chroma_client.get_or_create_collection(name="contracts")
    return collection

if __name__ == "__main__":
    setup_chromadb()
