from __future__ import annotations

import json
from importlib import import_module
from typing import Optional

from .. import types
from ..error import Error
from .file import read_file, write_file
from .path import infer_format


def read_dict(
    path: str, *, format: Optional[str] = None, basepath: Optional[str] = None
) -> types.IDict:
    if not format:
        format = infer_format(path, raise_missing=True)
    text = read_file(path, basepath=basepath)
    data = load_dict(text, format=format)
    return data


def write_dict(path: str, data: types.IDict, *, format: Optional[str] = None):
    if not format:
        format = infer_format(path, raise_missing=True)
    text = dump_dict(data, format=format)
    write_file(path, text)


def load_dict(text: str, *, format: str) -> types.IDict:
    try:
        if format == "json":
            return json.loads(text)
        elif format == "yaml":
            yaml = import_module("yaml")
            return yaml.safe_load(text)
    except Exception:
        raise Error(f'Cannot load "{format}" data from text: {text}')
    raise Error(f"Cannot load data from text with format: {format}")


def dump_dict(data: types.IDict, *, format: str) -> str:
    try:
        if format == "json":
            return json.dumps(data, indent=2)
        elif format == "yaml":
            yaml = import_module("yaml")
            return yaml.dump(data)
    except Exception:
        raise Error(f'Cannot dump "{format}" text from data: {data}')
    raise Error(f"Cannot dump data to text with format: {format}")


def clean_dict(data: types.IDict):
    for key, value in list(data.items()):
        if isinstance(value, dict):
            clean_dict(value)  # type: ignore
        elif isinstance(value, list):
            for item in value:  # type: ignore
                if isinstance(item, dict):
                    clean_dict(item)  # type: ignore
        if value is None or value == [] or value == {}:
            data.pop(key)
