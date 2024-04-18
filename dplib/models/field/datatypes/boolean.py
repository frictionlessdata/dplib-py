from __future__ import annotations

from typing import List, Literal, Optional

import pydantic

from ..constraints import BaseConstraints
from .base import BaseField


class BooleanField(BaseField):
    """The field contains boolean (true/false) data."""

    type: Literal["boolean"] = "boolean"
    format: Optional[Literal["default"]] = None
    constraints: BaseConstraints[bool] = pydantic.Field(default_factory=BaseConstraints)

    trueValues: List[str] = ["true", "True", "TRUE", "1"]
    """
    Values to be interpreted as “true” for boolean fields
    """

    falseValues: List[str] = ["false", "False", "FALSE", "0"]
    """
    Values to be interpreted as “false” for boolean fields
    """
