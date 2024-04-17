from __future__ import annotations

from typing import Literal, Optional

import pydantic

from ..constraints import JsonConstraints
from .base import BaseField


class ArrayField(BaseField):
    type: Literal["array"] = "array"
    format: Optional[Literal["default"]] = None
    constraints: JsonConstraints = pydantic.Field(default_factory=JsonConstraints)
