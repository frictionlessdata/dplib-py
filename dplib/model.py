from __future__ import annotations

import json
import pprint
from importlib import import_module
from typing import Optional

from pydantic import BaseModel
from typing_extensions import Self

from . import types
from .error import Error
from .helpers.file import infer_format, read_file, write_file


class Model(BaseModel, extra="forbid", validate_assignment=True):
    custom: types.IDict = {}

    def __str__(self) -> str:
        return repr(self)

    def __repr__(self) -> str:
        return pprint.pformat(self.to_dict(), sort_dicts=False)

    # Mappers

    def to_path(self, path: str, *, format: Optional[str] = None):
        format = format or infer_format(path)
        if not format:
            raise Error(f"Cannot infer format from path: {path}")
        text = self.to_text(format=format)
        write_file(path, text)

    @classmethod
    def from_path(cls, path: str, *, format: Optional[str] = None) -> Optional[Self]:
        format = format or infer_format(path)
        if not format:
            raise Error(f"Cannot infer format from path: {path}")
        text = read_file(path)
        return cls.from_text(text, format=format)  # type: ignore

    def to_text(self, *, format: str) -> str:
        data = self.to_dict()
        if format == "json":
            return json.dumps(data)
        elif format == "yaml":
            yaml = import_module("yaml")
            return yaml.dump(data)
        raise Error(f"Cannot convert to text for format: {format}")

    @classmethod
    def from_text(cls, text: str, *, format: str) -> Optional[Self]:
        if format == "json":
            data = json.loads(text)
            return cls.from_dict(data)
        elif format == "yaml":
            yaml = import_module("yaml")
            data = yaml.load(text)
            return cls.from_dict(data)
        raise Error(f"Cannot create from text with format: {format}")

    def to_dict(self):
        return self.model_dump(mode="json", exclude_unset=True, exclude_none=True)

    @classmethod
    def from_dict(cls, data: types.IDict) -> Optional[Self]:
        return cls(**data)
