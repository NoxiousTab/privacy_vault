# 🔐 PrivacyVault

> A secure, AI-powered local search engine for your personal documents.
> Upload files, ask natural language questions, and instantly get answers — all locally, with no data ever leaving your machine.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Streamlit](https://img.shields.io/badge/UI-Streamlit-orange)
![FAISS](https://img.shields.io/badge/Vector%20Search-FAISS-green)
![MiniLM](https://img.shields.io/badge/Embeddings-MiniLM-lightgrey)

---

## 🧠 How It Works

1. 📂 **Upload documents**: Supports `.txt`, `.pdf`, `.md`, and `.docx`
2. ✂️ **Chunk and embed**: Text is split into overlapping chunks and embedded with `MiniLM` or `MPNet`
3. 🧭 **Vector indexing**: Chunks are stored in a FAISS vector index
4. 🔍 **Semantic search**: Enter queries in plain English — PrivacyVault finds the most relevant document snippets
5. 🗂️ **Source-aware results**: Each match shows which file it came from

---

## 🚀 Quick Start

### 1. Clone the repo

```bash
git clone https://github.com/NoxiousTab/privacy_vault.git
cd privacy_vault
```
### 2. Set up your environment
```pip install -r requirements.txt```

### 3. Run the app
```streamlit run app.py```

