# Contract Clustering & Classification

## Overview
This project classifies and searches contracts using ChromaDB and machine learning. Users can upload contracts, classify them into categories (e.g., NDA, Vendor Contract), and find similar contracts using vector search.

## Features
- **Contract Classification**: Predicts contract type using a pretrained classifier.
- **Vector Search**: Finds similar contracts using embeddings stored in ChromaDB.
- **Configurable Embeddings**: Supports OpenAI (`text-embedding-ada-002`) or free local model (`all-MiniLM-L6-v2`).
- **Streamlit UI**: User-friendly web interface for search and classification.

## Setup
### Using Docker (Recommended)
```sh
docker-compose up --build
```

### Manual Setup
1. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
2. Run FastAPI backend:
   ```sh
   uvicorn api.main:app --reload
   ```
3. Run Streamlit UI:
   ```sh
   streamlit run ui/app.py
   ```

## API Endpoints
- `POST /classify/` → Classifies contract type and stores it.
- `POST /search/` → Finds similar contracts.
