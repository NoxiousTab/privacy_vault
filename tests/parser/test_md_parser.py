import pytest
from core.parser.md_parser import parse_md
from pathlib import Path

TEST_FILE = Path(__file__).parent / "data" / "sample1.md"

def test_parse_md_success():
    result = parse_md(str(TEST_FILE))

    expected = "# Sample Markdown\n\nThis is a **test** markdown file."

    assert result["filename"] == "sample1.md"
    assert result["content"] == expected
    assert result["word_count"] == len(expected.split())

def test_parse_md_file_not_found():
    with pytest.raises(FileNotFoundError):
        parse_md("nonexistent.md")

def test_parse_md_wrong_extension():
    fake_file = Path(__file__).parent / "data" / "not_a_md.txt"
    fake_file.write_text("Not a markdown file.")

    with pytest.raises(ValueError):
        parse_md(str(fake_file))

    fake_file.unlink()

# Optional auto-generation
def setup_module(module):
    if not TEST_FILE.exists():
        TEST_FILE.write_text("# Sample Markdown\n\nThis is a **test** markdown file.")
