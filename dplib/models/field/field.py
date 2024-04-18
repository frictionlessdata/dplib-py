from __future__ import annotations

from typing import Literal, Optional

import pydantic

from .constraints import BaseConstraints
from .datatypes import BaseField


class Field(BaseField):
    """Field with unspecified type."""

    type: Literal[None] = None
    format: Optional[Literal["default"]] = None
    constraints: BaseConstraints[str] = pydantic.Field(default_factory=BaseConstraints)
