import os
from core.parser.txt_parser import parse_txt
from core.parser.pdf_parser import parse_pdf
from core.parser.md_parser import parse_md
from core.chunker import chunk_text

from typing import List, Dict

def parse_file(filepath: str) -> Dict:
    ext = os.path.splitext(filepath)[-1].lower()

    if ext == ".txt":
        return parse_txt(filepath)
    elif ext == ".pdf":
        return parse_pdf(filepath)
    elif ext == ".md":
        return parse_md(filepath)
    elif ext == ".csv":
        return parse_csv(filepath)
    else:
        raise ValueError(f"Unsupported file extension: {ext}")

def load_and_chunk_files(filepaths: List[str]) -> List[Dict]:
    """
    Parse each file and return a flat list of chunk dicts.
    Each dict contains { "filename", "content" }
    """
    all_chunks = []

    for filepath in filepaths:
        parsed = parse_file(filepath)
        chunks = chunk_text(parsed["content"])
        for chunk in chunks:
            all_chunks.append({
                "filename": parsed["filename"],
                "content": chunk
            })

    return all_chunks
