import json
from pathlib import Path

import pytest

from dplib.error import Error
from dplib.models import Resource


def test_model_repr():
    resource = Resource.from_path("data/resource.json")
    assert str(resource) == "{'name': 'name', 'path': 'table.csv'}"


def test_model_custom_properties():
    data = {"name": "name", "extra": "value"}
    resource = Resource.from_dict(data)
    assert resource.name == "name"
    assert resource.custom["extra"] == "value"
    assert resource.to_dict() == data


def test_model_to_path(tmp_path: Path):
    path = str(tmp_path / "resource.json")
    resource = Resource.from_path("data/resource.json")
    resource.to_path(path)
    with open(path) as file:
        assert json.loads(file.read()) == {"name": "name", "path": "table.csv"}


def test_model_from_path_emtpy_file():
    with pytest.raises(Error) as excinfo:
        Resource.from_path("data/empty.json")
    error = excinfo.value
    assert str(error) == "The file is empty: data/empty.json"


def test_model_from_path_missing_file():
    with pytest.raises(Error) as excinfo:
        Resource.from_path("data/missing.json")
    error = excinfo.value
    assert str(error) == 'Cannot read file "data/missing.json"'


def test_model_from_path_not_supported_format():
    with pytest.raises(Error) as excinfo:
        Resource.from_path("data/text.txt")
    error = excinfo.value
    assert str(error) == "Cannot load data from text with format: txt"


def test_model_from_path_yaml():
    resource = Resource.from_path("data/resource.yaml")
    assert resource.name == "name"
    assert resource.path == "table.csv"


def test_model_to_path_yaml(tmp_path: Path):
    path = str(tmp_path / "resource.yaml")
    resource = Resource.from_path("data/resource.json")
    resource.to_path(path)
    with open(path) as file:
        assert file.read() == "name: name\npath: table.csv\n"
