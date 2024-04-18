from __future__ import annotations

from typing import Literal, Optional, Union

import pydantic

from ..constraints import BaseConstraints
from .base import BaseField

IGeojsonFormat = Union[
    Literal["default"],
    Literal["array"],
    Literal["object"],
]


class GeopointField(BaseField):
    """The field contains data describing a geographic point."""

    type: Literal["geopoint"] = "geopoint"
    format: Optional[IGeojsonFormat] = None
    constraints: BaseConstraints[str] = pydantic.Field(default_factory=BaseConstraints)
