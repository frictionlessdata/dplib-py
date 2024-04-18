from __future__ import annotations

from typing import Generic, Optional, TypeVar, Union

from .base import BaseConstraints

ValueType = TypeVar("ValueType")


# TODO: tweak serialization if needed
class ValueConstraints(BaseConstraints, Generic[ValueType]):
    minimum: Optional[Union[str, ValueType]] = None
    maximum: Optional[Union[str, ValueType]] = None
    exclusiveMinimum: Optional[Union[str, ValueType]] = None
    exclusiveMaximum: Optional[Union[str, ValueType]] = None
