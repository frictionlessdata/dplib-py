from __future__ import annotations

from typing import Literal, Optional

import pydantic

from ..constraints import JsonConstraints
from .base import BaseField


class ObjectField(BaseField):
    type: Literal["object"] = "object"
    format: Optional[Literal["default"]] = None
    constraints: JsonConstraints = pydantic.Field(default_factory=JsonConstraints)
