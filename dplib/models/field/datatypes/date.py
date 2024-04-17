from __future__ import annotations

from typing import Literal, Optional

import pydantic

from ..constraints import ValueConstraints
from .base import BaseField


class DateField(BaseField):
    type: Literal["date"] = "date"
    format: Optional[str] = None
    constraints: ValueConstraints = pydantic.Field(default_factory=ValueConstraints)
