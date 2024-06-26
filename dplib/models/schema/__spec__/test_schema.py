import pytest
from pydantic import ValidationError

from dplib import settings
from dplib.models import IntegerField, Schema


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


def test_schema_add_field():
    schema = Schema()
    schema.add_field(IntegerField(name="id"))
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


def test_schema_primary_key_v1():
    schema = Schema.from_dict({"primaryKey": "name"})
    assert schema.primaryKey == ["name"]


def test_schema_foreign_keys_v1():
    schema = Schema.from_dict(
        {"foreignKeys": [{"fields": "name", "reference": {"fields": "name"}}]}
    )
    assert schema.foreignKeys[0].fields == ["name"]
    assert schema.foreignKeys[0].reference.fields == ["name"]


def test_schema_to_dict():
    schema = Schema()
    assert schema.to_dict() == {
        "$schema": settings.PROFILE_CURRENT_SCHEMA,
    }
    schema.missingValues.append("x")  # type: ignore
    assert schema.to_dict() == {
        "$schema": settings.PROFILE_CURRENT_SCHEMA,
        "missingValues": ["", "x"],
    }
    schema.profile = settings.PROFILE_DEFAULT_SCHEMA
    assert schema.to_dict() == {
        "$schema": settings.PROFILE_DEFAULT_SCHEMA,
        "missingValues": ["", "x"],
    }


def test_schema_to_dict_with_fields():
    schema = Schema()
    schema.add_field(IntegerField(name="name"))
    assert schema.to_dict() == {
        "$schema": settings.PROFILE_CURRENT_SCHEMA,
        "fields": [
            {
                "name": "name",
                "type": "integer",
            }
        ],
    }
