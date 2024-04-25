from __future__ import annotations

import pprint
import warnings
from typing import Optional

from pydantic import BaseModel
from typing_extensions import Self

from .. import types
from ..error import Error
from ..helpers.dict import clean_dict, dump_dict, load_dict
from ..helpers.file import read_file, write_file
from ..helpers.path import ensure_basepath, infer_format


class Model(BaseModel, extra="allow", validate_assignment=True):
    def __str__(self) -> str:
        return repr(self)

    def __repr__(self) -> str:
        return pprint.pformat(self.to_dict(), sort_dicts=False)

    @property
    def custom(self) -> types.IDict:
        assert self.model_extra is not None
        return self.model_extra

    # Converters

    def to_path(self, path: str, *, format: Optional[str] = None):
        if not format:
            format = infer_format(path, raise_missing=True)
        text = self.to_text(format=format)
        write_file(path, text)

    @classmethod
    def from_path(
        cls, path: str, *, format: Optional[str] = None, basepath: Optional[str] = None
    ) -> Self:
        if not format:
            format = infer_format(path, raise_missing=True)
        path, basepath = ensure_basepath(path, basepath=basepath)
        text = read_file(path)
        if not text:
            raise Error(f"The file is empty: {path}")
        return cls.from_text(text, format=format, basepath=basepath)

    def to_text(self, *, format: str) -> str:
        data = self.to_dict()
        text = dump_dict(data, format=format)
        return text

    @classmethod
    def from_text(cls, text: str, *, format: str, basepath: Optional[str] = None) -> Self:
        data = load_dict(text, format=format)
        return cls.from_dict(data, basepath=basepath)

    def to_dict(self):
        data = self.model_dump(
            mode="json", by_alias=True, exclude_none=True, exclude_defaults=True
        )
        clean_dict(data)
        return data

    @classmethod
    def from_dict(cls, data: types.IDict, *, basepath: Optional[str] = None) -> Self:
        if basepath and cls.model_fields.get("basepath"):
            data["basepath"] = basepath
        return cls(**data)


# Although pydantic@2 moved all the model methods to the "model_" namespace
# the "schema" method is still in the root namespace
# https://github.com/pydantic/pydantic/issues/5165
warnings.filterwarnings(
    action="ignore",
    category=UserWarning,
    module=r"pydantic.*",
    message=r".*schema.*",
)
