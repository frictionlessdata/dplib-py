from __future__ import annotations

from typing import Literal, Optional

import pydantic

from ..constraints import ValueConstraints
from .base import BaseField


class DatetimeField(BaseField):
    type: Literal["datetime"] = "datetime"
    format: Optional[str] = None
    constraints: ValueConstraints = pydantic.Field(default_factory=ValueConstraints)
