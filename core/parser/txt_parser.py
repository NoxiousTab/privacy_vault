from pathlib import Path

def parse_txt(file_path: str) -> dict:
    """
    Parses a .txt file and returns its content and metadata.
    
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
    
    if path.suffix.lower() != ".txt":
        raise ValueError("Only .txt files are supported by txt_parser.")
    
    with path.open("r", encoding="utf-8") as f:
        content = f.read()
    
    return {
        "filename": path.name,
        "content": content.strip(),
        "word_count": len(content.strip().split())
    }
