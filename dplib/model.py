from __future__ import annotations

import json
import pprint
from importlib import import_module
from typing import Optional

import fsspec  # type: ignore
from pydantic import BaseModel
from typing_extensions import Self

from . import types


class Model(BaseModel, extra="forbid", validate_assignment=True):
    custom: types.IDict = {}

    def __str__(self) -> str:
        return repr(self)

    def __repr__(self) -> str:
        return pprint.pformat(self.to_dict(), sort_dicts=False)

    # Mappers

    # TODO: rebase on tmp file (safe write)
    def to_path(self, path: str, *, format: str = "json"):
        text = self.to_text(format=format)
        with fsspec.open(path, "wt", encoding="utf-8") as file:  # type: ignore
            file.write(text)  # type: ignore

    @classmethod
    def from_path(cls, path: str, *, format: str = "json") -> Optional[Self]:
        with fsspec.open(path, "rt", encoding="utf-8") as file:  # type: ignore
            text = file.read()  # type: ignore
        return cls.from_text(text, format=format)  # type: ignore

    def to_text(self, *, format: str = "json") -> str:
        data = self.to_dict()
        if format == "json":
            return json.dumps(data)
        elif format == "yaml":
            yaml = import_module("yaml")
            return yaml.dump(data)
        raise ValueError(f"Unknown format: {format}")

    @classmethod
    def from_text(cls, text: str, *, format: str = "json") -> Optional[Self]:
        if format == "json":
            data = json.loads(text)
            return cls.from_dict(data)
        elif format == "yaml":
            yaml = import_module("yaml")
            data = yaml.load(text)
            return cls.from_dict(data)
        raise ValueError(f"Unknown format: {format}")

    def to_dict(self):
        return self.model_dump(mode="json", exclude_unset=True, exclude_none=True)

    @classmethod
    def from_dict(cls, data: types.IDict) -> Optional[Self]:
        return cls(**data)
