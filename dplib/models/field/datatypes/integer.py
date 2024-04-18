from __future__ import annotations

from typing import Literal, Optional

import pydantic

from ..constraints import ValueConstraints
from .base import BaseField


class IntegerField(BaseField):
    """The field contains integers - that is whole numbers."""

    type: Literal["integer"] = "integer"
    format: Optional[Literal["default"]] = None
    constraints: ValueConstraints[int] = pydantic.Field(default_factory=ValueConstraints)

    groupChar: Optional[str] = None
    """
    String whose value is used to group digits for integer/number fields
    """

    bareNumber: bool = True
    """
    If false leading and trailing non numbers will be removed for integer/number fields
    """
