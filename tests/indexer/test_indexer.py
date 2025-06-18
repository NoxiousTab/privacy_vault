# tests/indexer/test_indexer.py

import pytest
import numpy as np
from core.indexer import VectorIndex

def test_index_add_and_search():
    # Simulate 3 chunks with dummy 3D embeddings
    texts = ["chunk one", "chunk two", "chunk three"]
    vectors = np.array([
        [1.0, 0.0, 0.0],
        [0.9, 0.1, 0.0],
        [0.0, 1.0, 0.0]
    ], dtype="float32")

    query = np.array([[1.0, 0.0, 0.0]], dtype="float32")

    index = VectorIndex(dim=3)
    index.add(vectors, texts)
    results = index.search(query, top_k=2)

    assert len(results) == 2
    assert results[0][2] == "chunk one"  # Best match
