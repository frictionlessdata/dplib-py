from __future__ import annotations

from typing import Literal, Optional

import pydantic

from ..constraints import ValueConstraints
from .base import BaseField


class YearField(BaseField):
    """The field contains a calendar year."""

    type: Literal["year"] = "year"
    format: Optional[Literal["default"]] = None
    constraints: ValueConstraints[int] = pydantic.Field(default_factory=ValueConstraints)
