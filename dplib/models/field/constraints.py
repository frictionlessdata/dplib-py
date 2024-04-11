from __future__ import annotations

from typing import Any, List, Optional

from ... import types
from ...model import Model


class Constraints(Model):
    required: Optional[bool] = None
    unique: Optional[bool] = None
    enum: Optional[List[Any]] = None
    minimum: Optional[Any] = None
    maximum: Optional[Any] = None
    exclusiveMinimum: Optional[Any] = None
    exclusiveMaximum: Optional[Any] = None
    maximum: Optional[Any] = None
    minLength: Optional[int] = None
    maxLength: Optional[int] = None
    jsonSchema: Optional[types.IData] = None
    pattern: Optional[str] = None
