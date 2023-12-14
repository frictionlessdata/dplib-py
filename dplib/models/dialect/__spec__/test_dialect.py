import pytest
from pydantic import ValidationError

from dplib.models import Dialect


def test_dialect_from_path():
    dialect = Dialect.from_path("data/dialect.json")
    assert dialect.delimiter == ";"
    assert dialect.get_delimiter() == ";"


def test_dialect_from_path_full():
    dialect = Dialect.from_path("data/dialect-full.json")
    assert dialect.delimiter == ";"
    assert dialect.lineTerminator == "\r\n"
    assert dialect.quoteChar == "'"
    assert dialect.doubleQuote is True
    assert dialect.escapeChar == "\\"
    assert dialect.nullSequence == "NULL"
    assert dialect.skipInitialSpace is True
    assert dialect.header is False
    assert dialect.commentChar == "#"


def test_dialect_defaults():
    dialect = Dialect()
    assert dialect.get_delimiter() == ","
    assert dialect.get_line_terminator() == "\r\n"
    assert dialect.get_quote_char() == '"'
    assert dialect.get_double_quote() is True
    assert dialect.get_header() is True


def test_dialect_from_text():
    text = '{"delimiter": ";"}'
    dialect = Dialect.from_text(text, format="json")
    assert dialect.delimiter == ";"


def test_dialect_from_dict():
    data = {"delimiter": ";"}
    dialect = Dialect.from_dict(data)
    assert dialect.delimiter == ";"


def test_dialect_from_dict_invalid():
    data = {"delimiter": 1}
    with pytest.raises(ValidationError):
        Dialect.from_dict(data)


def test_dialect_set_proprty_invalid():
    dialect = Dialect()
    with pytest.raises(ValidationError):
        dialect.delimiter = 1  # type: ignore


@pytest.mark.vcr
def test_dialect_profile():
    dialect = Dialect.from_path("data/dialect-full.json")
    profile = dialect.get_profile()
    assert profile
    assert profile.jsonSchema.get("title") == "CSV Dialect"
