from __future__ import annotations

from typing import Literal

import pydantic

from ..constraints import BaseConstraints
from .base import BaseField


class AnyField(BaseField):
    type: Literal["any"] = "any"
    constraints: BaseConstraints = pydantic.Field(default_factory=BaseConstraints)
