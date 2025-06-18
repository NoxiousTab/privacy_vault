import fitz  # PyMuPDF
from pathlib import Path

def parse_pdf(file_path: str) -> dict:
    """
    Parses a .pdf file and returns its content and metadata.
    
    Returns:
        {
            "filename": ...,
            "content": ...,
            "word_count": ...
        }
    """
    path = Path(file_path)
    
    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")
    
    if path.suffix.lower() != ".pdf":
        raise ValueError("Only .pdf files are supported by pdf_parser.")
    
    doc = fitz.open(file_path)
    content = ""
    
    for page in doc:
        content += page.get_text()

    doc.close()

    return {
        "filename": path.name,
        "content": content.strip(),
        "word_count": len(content.strip().split())
    }
