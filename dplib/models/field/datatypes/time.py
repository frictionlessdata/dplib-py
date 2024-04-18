from __future__ import annotations

import datetime
from typing import Literal, Optional

import pydantic

from ..constraints import ValueConstraints
from .base import BaseField


class TimeField(BaseField):
    """The field contains a time without a date."""

    type: Literal["time"] = "time"
    format: Optional[str] = None
    constraints: ValueConstraints[datetime.time] = pydantic.Field(
        default_factory=ValueConstraints
    )
