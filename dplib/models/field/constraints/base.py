from __future__ import annotations

from typing import Generic, List, Optional, TypeVar, Union

from ....system import Model

NativeType = TypeVar("NativeType")


class BaseConstraints(Model, Generic[NativeType]):
    required: Optional[bool] = None
    unique: Optional[bool] = None
    enum: Optional[List[Union[str, NativeType]]] = None
