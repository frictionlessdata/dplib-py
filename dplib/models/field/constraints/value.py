from __future__ import annotations

from typing import Generic, Optional, TypeVar, Union

from .base import BaseConstraints

NativeType = TypeVar("NativeType")


# TODO: tweak serialization if needed
class ValueConstraints(BaseConstraints[NativeType], Generic[NativeType]):
    minimum: Optional[Union[str, NativeType]] = None
    maximum: Optional[Union[str, NativeType]] = None
    exclusiveMinimum: Optional[Union[str, NativeType]] = None
    exclusiveMaximum: Optional[Union[str, NativeType]] = None
