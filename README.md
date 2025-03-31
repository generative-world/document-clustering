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


# 📜 Legal Contract Clustering Use Cases

This document outlines real-world use cases for clustering legal contract documents using AI and machine learning.

## 🚀 Use Cases

### 1️⃣ Contract Risk Assessment & Compliance Monitoring
**🔹 Use Case:** Identify contracts with potential legal risks or non-compliance issues.  
**📌 Example:** Automatically group contracts with high-risk clauses (e.g., indemnity, liability, termination) to flag them for legal review.  
**✅ Benefit:** Reduces compliance risks and improves regulatory adherence.

---

### 2️⃣ Contract Type Classification & Organization
**🔹 Use Case:** Automatically categorize contracts into predefined types.  
**📌 Example:** Cluster contracts into groups like **NDAs, employment agreements, vendor contracts, lease agreements, M&A contracts** etc.  
**✅ Benefit:** Helps legal teams quickly retrieve and analyze contracts of a similar type.

---

### 3️⃣ Clause Standardization & Deviation Detection
**🔹 Use Case:** Identify contracts with similar clauses and detect deviations.  
**📌 Example:** Group contracts with non-standard **indemnity** clauses that differ from the company's template.  
**✅ Benefit:** Ensures consistency and reduces negotiation risks.

---

### 4️⃣ Contract Renewal & Expiry Management
**🔹 Use Case:** Cluster contracts based on renewal dates and terms.  
**📌 Example:** Identify all contracts expiring within the next **three months**.  
**✅ Benefit:** Improves contract lifecycle management and prevents unintended expirations.

---

### 5️⃣ Legal Due Diligence in Mergers & Acquisitions (M&A)
**🔹 Use Case:** Speed up contract review in M&A processes by clustering similar agreements.  
**📌 Example:** Group all **vendor agreements** or **employment contracts** to streamline due diligence.  
**✅ Benefit:** Saves time in legal audits and facilitates efficient contract reviews.

---

### 6️⃣ Litigation & Dispute Resolution
**🔹 Use Case:** Identify patterns in contracts related to disputes.  
**📌 Example:** Cluster contracts containing **arbitration clauses vs. litigation clauses**.  
**✅ Benefit:** Helps legal teams analyze past disputes and refine contract drafting strategies.

---

### 7️⃣ Vendor & Supplier Contract Analysis
**🔹 Use Case:** Identify trends and risks in supplier agreements.  
**📌 Example:** Cluster contracts by key terms like **payment terms, penalties, or exclusivity**.  
**✅ Benefit:** Helps procurement teams negotiate better terms and reduce financial risks.

---

### 8️⃣ Data Privacy & GDPR Compliance
**🔹 Use Case:** Ensure all contracts meet data privacy requirements.  
**📌 Example:** Cluster contracts that involve **personal data processing** and check for missing GDPR compliance clauses.  
**✅ Benefit:** Enhances data protection and reduces legal exposure.

---

### 9️⃣ Contract Benchmarking & Best Practices
**🔹 Use Case:** Compare contract clauses across industries or competitors.  
**📌 Example:** Group contracts from different companies to analyze variations in **liability clauses**.  
**✅ Benefit:** Provides insights for drafting stronger contracts.

---

### 🔟 Automated Contract Summarization & AI-Powered Legal Research
**🔹 Use Case:** Improve document retrieval for lawyers by clustering similar contracts.  
**📌 Example:** If a lawyer is researching **"Force Majeure"** clauses, they can quickly access similar contracts where such clauses are present.  
**✅ Benefit:** Saves time in legal research and improves efficiency.

---

## 🏆 Conclusion
Using AI-driven clustering, legal teams can **streamline contract management, reduce risks, ensure compliance, and optimize contract analytics**. 🚀
