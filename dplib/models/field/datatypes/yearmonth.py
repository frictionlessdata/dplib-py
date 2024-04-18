from __future__ import annotations

from typing import Literal, Optional

import pydantic

from ..constraints import ValueConstraints
from .base import BaseField


class YearmonthField(BaseField):
    """The field contains a specific month of a specific year."""

    type: Literal["yearmonth"] = "yearmonth"
    format: Optional[Literal["default"]] = None
    constraints: ValueConstraints[str] = pydantic.Field(default_factory=ValueConstraints)
