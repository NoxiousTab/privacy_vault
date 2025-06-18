import pytest
from core.parser.txt_parser import parse_txt
from pathlib import Path

TEST_FILE = Path(__file__).parent / "data" / "sample1.txt"

def test_parse_txt_success():
    result = parse_txt(str(TEST_FILE))

    expected_content = (
        "This is a sample text file.\n"
        "It contains a few lines to test parsing functionality."
    )

    assert result["filename"] == "sample1.txt"
    assert result["content"] == expected_content
    assert result["word_count"] == len(expected_content.split())


def test_parse_txt_file_not_found():
    with pytest.raises(FileNotFoundError):
        parse_txt("nonexistent.txt")

def test_parse_txt_wrong_extension():
    fake_file = Path(__file__).parent / "data" / "fake.pdf"
    fake_file.write_text("fake content")  # create temporarily
    
    with pytest.raises(ValueError):
        parse_txt(str(fake_file))

    fake_file.unlink()  # cleanup
