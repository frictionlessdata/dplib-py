import pprint

from pydantic import BaseModel

from . import types


class Model(BaseModel, extra="forbid", validate_assignment=True):
    custom: types.IDict = {}

    def __str__(self) -> str:
        return repr(self)

    def __repr__(self) -> str:
        return pprint.pformat(self.to_dict(), sort_dicts=False)

    # Mappers

    @classmethod
    def from_path(cls, path: str, *, format: str = "json"):
        pass

    @classmethod
    def to_path(cls, path: str, *, format: str = "json"):
        pass

    @classmethod
    def from_text(cls, path: str, *, format: str = "json"):
        pass

    @classmethod
    def to_text(cls, path: str, *, format: str = "json"):
        pass

    @classmethod
    def from_dict(cls, data: types.IDict):
        return cls(**data)

    def to_dict(self):
        return self.model_dump(mode="json", exclude_unset=True, exclude_none=True)
