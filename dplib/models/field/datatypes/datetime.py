from __future__ import annotations

import datetime
from typing import Literal, Optional

import pydantic

from ..constraints import ValueConstraints
from .base import BaseField


class DatetimeField(BaseField):
    """The field contains a date with a time."""

    type: Literal["datetime"] = "datetime"
    format: Optional[str] = None
    constraints: ValueConstraints[datetime.datetime] = pydantic.Field(
        default_factory=ValueConstraints
    )
