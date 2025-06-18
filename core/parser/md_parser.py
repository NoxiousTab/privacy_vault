from pathlib import Path

def parse_md(file_path: str) -> dict:
    """
    Parses a markdown (.md) file and returns content and metadata.

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

    if path.suffix.lower() != ".md":
        raise ValueError("Only .md files are supported by md_parser.")
    
    content = path.read_text(encoding="utf-8").strip()

    return {
        "filename": path.name,
        "content": content,
        "word_count": len(content.split())
    }
