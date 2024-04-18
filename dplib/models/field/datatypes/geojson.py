from __future__ import annotations

from typing import Literal, Optional, Union

import pydantic

from ..constraints import BaseConstraints
from .base import BaseField

IGeojsonFormat = Union[
    Literal["default"],
    Literal["topojson"],
]


class GeojsonField(BaseField):
    """The field contains a JSON object according to GeoJSON or TopoJSON spec."""

    type: Literal["geojson"] = "geojson"
    format: Optional[IGeojsonFormat] = None
    constraints: BaseConstraints[str] = pydantic.Field(default_factory=BaseConstraints)
