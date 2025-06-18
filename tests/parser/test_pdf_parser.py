import pytest
from core.parser.pdf_parser import parse_pdf
from pathlib import Path

TEST_FILE = Path(__file__).parent / "data" / "sample1.pdf"
def test_parse_pdf_success():
    result = parse_pdf(str(TEST_FILE))

    expected_content = (
        "This is a sample text file.\n"
        "It contains a few words to test parsing functionality."
    )

    assert result["filename"] == "sample1.pdf"
    assert "sample text file" in result["content"]
    assert "test parsing functionality" in result["content"]
    assert result["word_count"] > 5

def test_parse_pdf_file_not_found():
    with pytest.raises(FileNotFoundError):
        parse_pdf("nonexistent.pdf")

def test_parse_pdf_wrong_extension():
    fake_file = Path(__file__).parent / "data" / "fake.txt"
    fake_file.write_text("fake content")

    with pytest.raises(ValueError):
        parse_pdf(str(fake_file))

    fake_file.unlink()
