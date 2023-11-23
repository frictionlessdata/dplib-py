from typing import Any, Dict, List

from pydantic import BaseModel, ValidationError
from pydantic_core import ErrorDetails


class Model(BaseModel, validate_assignment=True):
    def __str__(self):
        return str(self.to_descriptor())

    @classmethod
    def validate_descriptor(cls, descriptor: Dict[str, Any]):
        errors: List[ErrorDetails] = []
        try:
            cls.model_validate(descriptor)
        except ValidationError as e:
            errors = e.errors()
        return errors

    @classmethod
    def from_descriptor(cls, descriptor: Dict[str, Any]):
        return cls(**descriptor)

    def to_descriptor(self):
        return self.model_dump(exclude_unset=True, exclude_none=True)
