import pprint
from typing import Any, Dict, List

from pydantic import BaseModel, ValidationError
from pydantic_core import ErrorDetails

from . import types


class Model(BaseModel, extra="forbid", validate_assignment=True):
    custom: types.IData = {}

    def __str__(self) -> str:
        return repr(self)

    def __repr__(self) -> str:
        return pprint.pformat(self.to_dict(), sort_dicts=False)

    # Validators

    # TODO: rebase on validate_yaml/json/dict?
    @classmethod
    def validate_descriptor(cls, descriptor: Dict[str, Any]):
        errors: List[ErrorDetails] = []
        try:
            cls.model_validate(descriptor)
        except ValidationError as e:
            errors = e.errors()
        return errors

    # Mappers

    @classmethod
    def from_yaml(cls, path: str):
        pass

    @classmethod
    def to_yaml(cls, path: str):
        pass

    @classmethod
    def from_json(cls, path: str):
        pass

    @classmethod
    def to_json(cls, path: str):
        pass

    @classmethod
    def from_dict(cls, data: types.IData):
        return cls(**data)

    def to_dict(self):
        return self.model_dump(mode="json", exclude_unset=True, exclude_none=True)
