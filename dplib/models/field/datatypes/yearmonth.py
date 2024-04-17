from __future__ import annotations

from typing import Literal, Optional

import pydantic

from ..constraints import ValueConstraints
from .base import BaseField


class YearmonthField(BaseField):
    type: Literal["yearmonth"] = "yearmonth"
    format: Optional[Literal["default"]] = None
    constraints: ValueConstraints = pydantic.Field(default_factory=ValueConstraints)
