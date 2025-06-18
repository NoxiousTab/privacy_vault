from typing import List

def chunk_text(text: str, chunk_size: int = 300, overlap: int = 50) -> List[str]:
    """
    Splits text into overlapping chunks to preserve context.

    Args:
        text (str): The full text content.
        max_tokens (int): Approximate max tokens per chunk.
        overlap (int): Overlapping token count between chunks.

    Returns:
        List[str]: List of text chunks.
    """
    # replace chunk_size with max_tokens for the commented code

    words = text.split()
    chunks = []
    '''start = 0

    while start < len(words):
        end = min(start + max_tokens, len(words))
        chunk = " ".join(words[start:end])
        chunks.append(chunk)
        start += max_tokens - overlap'''

    for i in range(0, len(words), chunk_size - overlap):
        chunk = " ".join(words[i:i + chunk_size])
        chunks.append(chunk)


    return chunks
