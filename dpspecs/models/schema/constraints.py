from typing import Any, List, Optional

from ...model import Model


class BaseConstraints(Model):
    required: Optional[bool] = None
    unique: Optional[bool] = None
    enum: Optional[List[Any]] = None


class ValueConstraints(BaseConstraints):
    minimum: Optional[str] = None
    maximum: Optional[str] = None


class CollectionConstraints(BaseConstraints):
    minLength: Optional[int] = None
    maxLength: Optional[int] = None


class StringConstraints(CollectionConstraints):
    pattern: Optional[str] = None
