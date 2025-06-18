import pytest
from core.embedding import Embedder
import numpy as np

def test_embedder_output_shape():
    texts = ["This is a test.", "Another chunk here."]
    embedder = Embedder()
    vectors = embedder.embed(texts)

    assert isinstance(vectors, np.ndarray)
    assert vectors.shape[0] == len(texts)
    assert vectors.shape[1] > 0  # Should be 384 for MiniLM-L6-v2

def test_embedder_same_input_same_output():
    texts = ["reproducible sentence"]
    embedder = Embedder()
    vec1 = embedder.embed(texts)
    vec2 = embedder.embed(texts)

    assert np.allclose(vec1, vec2)
