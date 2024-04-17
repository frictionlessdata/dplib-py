from __future__ import annotations

from typing import Literal, Optional

import pydantic

from ..constraints import ValueConstraints
from .base import BaseField


class TimeField(BaseField):
    type: Literal["time"] = "time"
    format: Optional[str] = None
    constraints: ValueConstraints = pydantic.Field(default_factory=ValueConstraints)
