from __future__ import annotations

import pprint
import warnings
from functools import cached_property
from typing import Any, Optional

from pydantic import BaseModel
from typing_extensions import Self

from . import types
from .error import Error
from .helpers.data import clean_data, dump_data, load_data, read_data, write_data
from .helpers.path import infer_basepath, join_basepath


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
        data = self.to_dict()
        write_data(path, data, format=format)

    @classmethod
    def from_path(
        cls, path: str, *, format: Optional[str] = None, basepath: Optional[str] = None
    ) -> Self:
        if basepath:
            path = join_basepath(path, basepath)
        else:
            basepath = infer_basepath(path)
        data = read_data(path, format=format)
        return cls.from_dict(data, basepath=basepath)

    def to_text(self, *, format: str) -> str:
        data = self.to_dict()
        text = dump_data(data, format=format)
        return text

    @classmethod
    def from_text(cls, text: str, *, format: str, basepath: Optional[str] = None) -> Self:
        data = load_data(text, format=format)
        return cls.from_dict(data, basepath=basepath)

    def to_dict(self):
        data = self.model_dump(mode="json")
        clean_data(data)
        return data

    @classmethod
    def from_dict(cls, data: types.IDict, *, basepath: Optional[str] = None) -> Self:
        if basepath and cls.model_fields.get("basepath"):
            data["basepath"] = basepath
        return cls(**data)

    def to_dp(self) -> Model:
        raise Error(f'Cannot convert "{type(self).__name__}" to data package notation')

    @classmethod
    def from_dp(cls, model: Any, /) -> Model:
        raise Error(f'Cannot convert "{cls.__name__}" from data package notation')


# Although pydantic@2 moved all the model methods to the "model_" namespace
# the "schema" method is still in the root namespace
# https://github.com/pydantic/pydantic/issues/5165
warnings.filterwarnings(
    action="ignore",
    category=UserWarning,
    module=r"pydantic.*",
    message=r".*schema.*",
)
