import pytest
from pydantic import ValidationError

from dplib.models import Field, Schema


def test_schema_from_path():
    schema = Schema.from_path("data/schema.json")
    assert len(schema.fields) == 2
    assert schema.fields[0].name == "id"
    assert schema.fields[0].type == "integer"
    assert schema.fields[1].name == "name"
    assert schema.fields[1].type == "string"


def test_schema_from_path_full():
    schema = Schema.from_path("data/schema-full.json")
    assert len(schema.fields) == 15
    assert len(schema.primaryKey) == 4
    assert len(schema.foreignKeys) == 1
    assert schema.foreignKeys[0].fields == ["position_title"]
    assert schema.foreignKeys[0].reference.resource == "positions"
    assert schema.foreignKeys[0].reference.fields == ["name"]


def test_schema_defaults():
    schema = Schema()
    assert schema.missingValues == [""]


def test_schema_from_text():
    text = '{"missingValues": ["x"]}'
    schema = Schema.from_text(text, format="json")
    assert schema.missingValues == ["x"]


def test_schema_from_dict():
    data = {"missingValues": ["x"]}
    schema = Schema.from_dict(data)
    assert schema.missingValues == ["x"]


def test_schema_from_dict_invalid():
    data = {"missingValues": 1}
    with pytest.raises(ValidationError):
        Schema.from_dict(data)


def test_schema_set_proprty_invalid():
    schema = Schema()
    with pytest.raises(ValidationError):
        schema.missingValues = 1  # type: ignore


@pytest.mark.vcr
def test_schema_profile():
    schema = Schema.from_path("data/schema-full.json")
    profile = schema.get_profile()
    assert profile
    assert profile.jsonSchema.get("title") == "Table Schema"


def test_schema_add_field():
    schema = Schema()
    schema.add_field(Field(name="id", type="integer"))
    field = schema.get_field(name="id")
    assert field
    assert field.name == "id"
    assert field.type == "integer"


def test_schema_get_field():
    schema = Schema.from_path("data/schema.json")
    field = schema.get_field(name="id")
    assert field
    assert field.name == "id"
    assert field.type == "integer"


def test_schema_to_dict():
    schema = Schema()
    assert schema.to_dict() == {}
    schema.missingValues.append("x")
    assert schema.to_dict() == {"missingValues": ["", "x"]}
