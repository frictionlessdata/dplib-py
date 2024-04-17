from __future__ import annotations

from typing import Literal, Optional

import pydantic

from ..constraints import EnumerableConstraints
from .base import BaseField


class IntegerField(BaseField):
    type: Literal["integer"] = "integer"
    format: Optional[Literal["default"]] = None
    constraints: EnumerableConstraints = pydantic.Field(
        default_factory=EnumerableConstraints
    )

    bareNumber: Optional[bool] = None
    """
    If false leading and trailing non numbers will be removed for integer/number fields
    """

    groupChar: Optional[str] = None
    """
    String whose value is used to group digits for integer/number fields
    """
