from typing import Any, Generic, List, Optional, TypeVar

from ...model import Model

T = TypeVar("T")


class BaseConstraints(Model):
    required: Optional[bool] = None
    unique: Optional[bool] = None
    enum: Optional[List[Any]] = None


class ValueConstraints(BaseConstraints, Generic[T]):
    minimum: Optional[T] = None
    maximum: Optional[T] = None


class CollectionConstraints(BaseConstraints):
    minLength: Optional[int] = None
    maxLength: Optional[int] = None


class StringConstraints(CollectionConstraints):
    pattern: Optional[str] = None
