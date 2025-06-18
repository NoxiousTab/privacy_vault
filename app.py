import streamlit as st
from core.parser.loader import load_and_chunk_files
from core.embedding import Embedder
from core.indexer import VectorIndex
from core.semantic_search import SemanticSearchEngine

import tempfile
import os

st.set_page_config(page_title="PrivacyVault", layout="wide")

st.title("🔐 PrivacyVault")
st.markdown("Upload your personal documents and search them with AI.")

uploaded_files = st.file_uploader("Upload files", type=["txt", "pdf", "md", "csv"], accept_multiple_files=True)

if uploaded_files:
    st.success(f"{len(uploaded_files)} file(s) uploaded!")

    with st.spinner("Processing and indexing files..."):


        with tempfile.TemporaryDirectory() as tmpdir:
            filepaths = []
            for file in uploaded_files:
                filepath = os.path.join(tmpdir, file.name)
                with open(filepath, "wb") as f:
                    f.write(file.read())
                filepaths.append(filepath)

            chunks = load_and_chunk_files(filepaths)


            embedder = Embedder("all-mpnet-base-v2")
            vectors = embedder.embed([chunk["content"] for chunk in chunks]).astype("float32")

            index = VectorIndex(dim=vectors.shape[1])
            index.add(vectors, chunks)

            search_engine = SemanticSearchEngine(embedder, index)

        st.success("✅ Files indexed successfully!")

        # Query section
        query = st.text_input("Ask a question or enter a search query:")
        if query:
            with st.spinner("Searching..."):
                results = search_engine.search(query, top_k=5)
            st.markdown("### 🔎 Top Matches:")
            for i, (idx, score, chunk) in enumerate(results):
                st.markdown(f"**{i+1}.** `{score:.2f}` — 🗂️ *{chunk['filename']}*")
                st.markdown(f"> {chunk['content'][:500]}{'...' if len(chunk['content']) > 500 else ''}")

