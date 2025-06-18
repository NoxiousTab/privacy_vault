from docx import Document
from pathlib import Path

def parse_docx(file_path: str) -> dict:
    """
    Parses a .docx file and returns its content and metadata.

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
    
    if path.suffix.lower() != ".docx":
        raise ValueError("Only .docx files are supported by docx_parser.")
    
    document = Document(file_path)
    paragraphs = [p.text.strip() for p in document.paragraphs if p.text.strip()]
    content = "\n".join(paragraphs)

    return {
        "filename": path.name,
        "content": content,
        "word_count": len(content.split())
    }
