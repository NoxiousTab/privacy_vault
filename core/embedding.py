from sentence_transformers import SentenceTransformer
from typing import List
import numpy as np

class Embedder:
    def __init__(self, model_name: str = "all-mpnet-base-v2"):
        self.model = SentenceTransformer(model_name)

    def embed(self, texts: List[str]) -> np.ndarray:
        """
        Returns vector embeddings for a list of text chunks.

        Args:
            texts (List[str]): List of strings.

        Returns:
            np.ndarray: 2D array of shape (len(texts), embedding_dim)
        """
        return np.array(self.model.encode(texts, show_progress_bar=False, convert_to_numpy=True))
