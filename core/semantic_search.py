from core.embedding import Embedder
from core.indexer import VectorIndex
import numpy as np
from typing import List, Tuple

class SemanticSearchEngine:
    def __init__(self, embedder: Embedder, index: VectorIndex):
        self.embedder = embedder
        self.index = index

    def search(self, query: str, top_k: int = 5) -> List[Tuple[int, float, str]]:
        """
        Embeds the query and searches the index.

        Returns:
            List of (index, score, chunk_text)
        """
        query_vec = self.embedder.embed([query]).astype("float32")
        return self.index.search(query_vec, top_k=top_k)
