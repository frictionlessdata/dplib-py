from __future__ import annotations

from typing import Literal, Optional

import pydantic

from ..constraints import ValueConstraints
from .base import BaseField


class NumberField(BaseField):
    type: Literal["number"] = "number"
    format: Optional[Literal["default"]] = None
    constraints: ValueConstraints = pydantic.Field(default_factory=ValueConstraints)

    bareNumber: Optional[bool] = None
    """
    If false leading and trailing non numbers will be removed for integer/number fields
    """

    groupChar: Optional[str] = None
    """
    String whose value is used to group digits for integer/number fields
    """

    decimalChar: Optional[str] = None
    """
    String whose value is used to represent a decimal point for number fields
    """
