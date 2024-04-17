from __future__ import annotations

from typing import Literal, Optional

import pydantic

from ..constraints import BaseConstraints
from .base import BaseField


class GeojsonField(BaseField):
    type: Literal["geojson"] = "geojson"
    format: Optional[Literal["default"]] = None
    constraints: BaseConstraints = pydantic.Field(default_factory=BaseConstraints)
