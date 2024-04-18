from __future__ import annotations

from typing import Literal, Optional

import pydantic

from ..constraints import BaseConstraints
from .base import BaseField


class AnyField(BaseField):
    """The field contains values of a unspecified or mixed type."""

    type: Literal["any"] = "any"
    format: Optional[Literal["default"]] = None
    constraints: BaseConstraints[str] = pydantic.Field(default_factory=BaseConstraints)
