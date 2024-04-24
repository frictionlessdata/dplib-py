from pathlib import Path

import pytest
from pydantic import ValidationError

from dplib import settings
from dplib.models import Dialect, Resource, Schema


def test_resource_from_path():
    resource = Resource.from_path("data/resource.json")
    assert resource.name == "name"
    assert resource.path == "table.csv"


def test_resource_from_path_full():
    resource = Resource.from_path("data/resource-full.json")
    assert resource.name == "name"
    assert resource.type == "table"
    assert resource.path == "table.csv"
    assert resource.title == "title"
    assert resource.description == "description"
    assert resource.format == "csv"
    assert resource.mediatype == "text/csv"
    assert resource.encoding == "utf-8"
    assert resource.bytes == 100
    dialect = resource.get_dialect()
    assert dialect
    assert dialect.delimiter == ";"
    schema = resource.get_schema()
    assert schema
    assert len(schema.fields) == 2


def test_resource_from_text():
    text = '{"name": "name"}'
    resource = Resource.from_text(text, format="json")
    assert resource.name == "name"


def test_resource_from_dict():
    data = {"name": "name"}
    resource = Resource.from_dict(data)
    assert resource.name == "name"


def test_resource_from_dict_invalid():
    data = {"name": 1}
    with pytest.raises(ValidationError):
        Resource.from_dict(data)


def test_resource_set_proprty_invalid():
    resource = Resource()
    with pytest.raises(ValidationError):
        resource.name = 1  # type: ignore


def test_resource_get_fullpath():
    resource = Resource.from_path("data/resource.json")
    fullpath = resource.get_fullpath()
    assert fullpath == str(Path("data/table.csv"))


def test_resource_get_fullpath_with_basepath():
    resource = Resource(path="table.csv", basepath="data")
    fullpath = resource.get_fullpath()
    assert fullpath == str(Path("data/table.csv"))


def test_resource_get_source():
    resource = Resource(data=[])
    source = resource.get_source()
    assert source == []


def test_resource_dialect_inline():
    resource = Resource(dialect=Dialect(delimiter=";"))
    dialect = resource.get_dialect()
    assert dialect
    assert dialect.delimiter == ";"


def test_resource_schema_inline():
    resource = Resource(schema=Schema.from_path("data/schema.json"))
    schema = resource.get_schema()
    assert schema
    assert len(schema.fields) == 2


def test_resource_hash():
    resource = Resource(hash="hash")
    hash = resource.get_hash()
    assert hash
    assert hash.type == "md5"
    assert hash.value == "hash"
    assert hash.short == "hash"
    assert hash.long == "md5:hash"


def test_resource_hash_non_default_type():
    resource = Resource(hash="sha256:hash")
    hash = resource.get_hash()
    assert hash
    assert hash.type == "sha256"
    assert hash.value == "hash"
    assert hash.short == "sha256:hash"
    assert hash.long == "sha256:hash"


def test_resource_dereference():
    resource = Resource.from_path("data/resource-full.json")
    resource.dereference()
    assert isinstance(resource.dialect, Dialect)
    assert resource.dialect.delimiter == ";"
    assert isinstance(resource.schema, Schema)
    assert len(resource.schema.fields) == 2


def test_resource_contributors_role_v1():
    resource = Resource.from_dict({"contributors": [{"role": "author"}]})
    assert resource.contributors[0].custom == {}
    assert resource.contributors[0].roles == ["author"]


def test_resource_to_dict():
    resource = Resource()
    assert resource.to_dict() == {
        "$schema": settings.PROFILE_CURRENT_RESOURCE,
    }
    resource.name = "name"
    assert resource.to_dict() == {
        "$schema": settings.PROFILE_CURRENT_RESOURCE,
        "name": "name",
    }
    resource.profile = settings.PROFILE_DEFAULT_RESOURCE
    assert resource.to_dict() == {
        "$schema": settings.PROFILE_DEFAULT_RESOURCE,
        "name": "name",
    }
