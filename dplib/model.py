from __future__ import annotations

import json
import pprint
import warnings
from functools import cached_property
from importlib import import_module
from typing import Optional

from pydantic import BaseModel
from typing_extensions import Self

from . import types
from .error import Error
from .helpers.file import infer_format, read_file, write_file
from .helpers.struct import clean_dict


class Model(BaseModel, extra="allow", validate_assignment=True):
    def __str__(self) -> str:
        return repr(self)

    def __repr__(self) -> str:
        return pprint.pformat(self.to_dict(), sort_dicts=False)

    @cached_property
    def custom(self) -> types.IDict:
        assert self.model_extra is not None
        return self.model_extra

    # Converters

    def to_path(self, path: str, *, format: Optional[str] = None):
        format = format or infer_format(path)
        if not format:
            raise Error(f"Cannot infer format from path: {path}")
        text = self.to_text(format=format)
        write_file(path, text)

    @classmethod
    def from_path(cls, path: str, *, format: Optional[str] = None) -> Self:
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
    def from_text(cls, text: str, *, format: str) -> Self:
        if format == "json":
            data = json.loads(text)
            return cls.from_dict(data)
        elif format == "yaml":
            yaml = import_module("yaml")
            data = yaml.load(text)
            return cls.from_dict(data)
        raise Error(f"Cannot create from text with format: {format}")

    def to_dict(self):
        data = self.model_dump(mode="json")
        clean_dict(data)
        return data

    @classmethod
    def from_dict(cls, data: types.IDict) -> Self:
        return cls(**data)


# Although pydantic@2 moved all the model methods to the "model_" namespace
# the "schema" method is still in the root namespace
warnings.filterwarnings(
    action="ignore",
    category=UserWarning,
    module=r"pydantic.*",
    message=r".*schema.*",
)
