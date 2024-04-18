from __future__ import annotations

from typing import Literal, Optional

import pydantic

from ..constraints import ValueConstraints
from .base import BaseField


class DurationField(BaseField):
    """The field contains a duration of time."""

    type: Literal["duration"] = "duration"
    format: Optional[Literal["default"]] = None
    constraints: ValueConstraints[str] = pydantic.Field(default_factory=ValueConstraints)
