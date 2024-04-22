import pytest
from pydantic import ValidationError

from dplib import settings
from dplib.models import Dialect


def test_dialect_from_path():
    dialect = Dialect.from_path("data/dialect.json")
    assert dialect.delimiter == ";"


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
    assert dialect.header is True
    assert dialect.headerJoin == " "
    assert dialect.delimiter == ","
    assert dialect.lineTerminator == "\r\n"
    assert dialect.quoteChar == '"'
    assert dialect.doubleQuote is True
    assert dialect.sheetNumber == 1


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


def test_dialect_to_dict():
    dialect = Dialect()
    assert dialect.to_dict() == {
        "$schema": settings.PROFILE_CURRENT_DIALECT,
    }
    dialect.delimiter = ";"
    assert dialect.to_dict() == {
        "$schema": settings.PROFILE_CURRENT_DIALECT,
        "delimiter": ";",
    }
    dialect.profile = settings.PROFILE_DEFAULT_DIALECT
    assert dialect.to_dict() == {
        "$schema": settings.PROFILE_DEFAULT_DIALECT,
        "delimiter": ";",
    }
