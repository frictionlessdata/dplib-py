from __future__ import annotations

from typing import Literal, Optional

import pydantic

from ..constraints import JsonConstraints
from .base import BaseField


class ArrayField(BaseField):
    """The field contains a valid JSON array."""

    type: Literal["array"] = "array"
    format: Optional[Literal["default"]] = None
    constraints: JsonConstraints = pydantic.Field(default_factory=JsonConstraints)
