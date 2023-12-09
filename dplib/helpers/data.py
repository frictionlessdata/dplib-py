import json
from importlib import import_module

from .. import types
from ..error import Error


def load_data(text: str, *, format: str) -> types.IDict:
    if format == "json":
        return json.loads(text)
    elif format == "yaml":
        yaml = import_module("yaml")
        data = yaml.load(text)
        return data
    raise Error(f"Cannot load data from text with format: {format}")


def dump_data(data: types.IDict, *, format: str) -> str:
    if format == "json":
        return json.dumps(data)
    elif format == "yaml":
        yaml = import_module("yaml")
        return yaml.dump(data)
    raise Error(f"Cannot dump data to text with format: {format}")


def clean_data(data: types.IDict):
    for key, value in list(data.items()):
        if isinstance(value, dict):
            clean_dict(value)  # type: ignore
        elif isinstance(value, list):
            for item in value:  # type: ignore
                if isinstance(item, dict):
                    clean_dict(item)  # type: ignore
        if value is None or value == [] or value == {}:
            data.pop(key)
        elif isinstance(value, list) and not any(value):  # type: ignore
            data.pop(key)
