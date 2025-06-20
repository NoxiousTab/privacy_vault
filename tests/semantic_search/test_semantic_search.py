from core.embedding import Embedder
from core.indexer import VectorIndex
from core.semantic_search import SemanticSearchEngine
import numpy as np

def test_semantic_search_basic():
    embedder = Embedder("all-MiniLM-L6-v2")

    texts = [
        "Python is a programming language.",
        "Cats are great pets.",
        "The Earth revolves around the Sun."
    ]
    vectors = embedder.embed(texts).astype("float32")

    index = VectorIndex(dim=vectors.shape[1])
    index.add(vectors, texts)

    engine = SemanticSearchEngine(embedder, index)
    results = engine.search("Tell me about animals", top_k=2)

    assert len(results) == 2
    assert any("Cats" in r[2] for r in results)
