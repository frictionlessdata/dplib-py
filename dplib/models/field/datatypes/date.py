from __future__ import annotations

import datetime
from typing import Literal, Optional

import pydantic

from ..constraints import ValueConstraints
from .base import BaseField


class DateField(BaseField):
    """he field contains a date without a time."""

    type: Literal["date"] = "date"
    format: Optional[str] = None
    constraints: ValueConstraints[datetime.date] = pydantic.Field(
        default_factory=ValueConstraints
    )
