from __future__ import annotations

from typing import Literal, Optional

import pydantic

from ..constraints import ValueConstraints
from .base import BaseField


class NumberField(BaseField):
    """The field contains numbers of any kind including decimals."""

    type: Literal["number"] = "number"
    format: Optional[Literal["default"]] = None
    constraints: ValueConstraints[float] = pydantic.Field(
        default_factory=ValueConstraints
    )

    decimalChar: str = "."
    """
    String whose value is used to represent a decimal point for number fields
    """

    groupChar: Optional[str] = None
    """
    String whose value is used to group digits for integer/number fields
    """

    bareNumber: bool = True
    """
    If false leading and trailing non numbers will be removed for integer/number fields
    """
