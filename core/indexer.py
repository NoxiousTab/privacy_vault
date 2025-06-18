import faiss
import numpy as np
from typing import List, Tuple, Dict

class VectorIndex:
    def __init__(self, dim: int):
        self.index = faiss.IndexFlatIP(dim)  # Inner Product (use with normalized vectors for cosine sim)
        self.chunk_metadata: List[Dict[str, str]] = []

    def add(self, vectors: np.ndarray, chunk_dicts: List[Dict[str, str]]):
        if len(vectors) != len(chunk_dicts):
            raise ValueError("Mismatch between number of vectors and metadata.")
        
        faiss.normalize_L2(vectors)
        self.index.add(vectors)
        self.chunk_metadata.extend(chunk_dicts)


    def search(self, query_vector: np.ndarray, top_k: int = 5) -> List[Tuple[int, float, Dict[str, str]]]:
        faiss.normalize_L2(query_vector)
        scores, indices = self.index.search(query_vector, top_k)

        results = []
        for i, score in zip(indices[0], scores[0]):
            if i == -1:
                continue
            results.append((i, score, self.chunk_metadata[i]))
        return results


