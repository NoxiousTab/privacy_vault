# tests/chunker/test_chunker.py

import pytest
from core.chunker import chunk_text

def test_chunk_text_basic():
    text = " ".join(f"word{i}" for i in range(1000))
    chunks = chunk_text(text, max_tokens=100, overlap=20)

    assert len(chunks) > 1
    assert all(isinstance(c, str) for c in chunks)
    assert all(len(c.split()) <= 100 for c in chunks)

def test_chunk_text_handles_short_text():
    text = "short text"
    chunks = chunk_text(text, max_tokens=100)
    assert len(chunks) == 1
    assert chunks[0] == text

def test_chunk_text_exact_length():
    text = " ".join(["word"] * 100)
    chunks = chunk_text(text, max_tokens=100, overlap=0)
    assert len(chunks) == 1
