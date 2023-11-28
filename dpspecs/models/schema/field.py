from __future__ import annotations

from typing import Any, Dict, List, Literal, Optional, Union

import pydantic

from ...model import Model
from .constraints import Constraints


class Field(Model):
    name: str
    type: FieldType = "any"
    title: Optional[str] = None
    description: Optional[str] = None
    format: Optional[str] = None
    missingValues: Optional[List[str]] = None
    constraints: Constraints = pydantic.Field(default_factory=Constraints)

    # Array
    arrayItem: Optional[Dict[str, Any]] = None

    # Boolean
    trueValues: Optional[List[str]] = None
    falseValues: Optional[List[str]] = None

    # Integer/Number
    bareNumber: Optional[bool] = None
    groupChar: Optional[str] = None
    decimalChar: Optional[str] = None


FieldType = Union[
    Literal["any"],
    Literal["array"],  # continue
    Literal["boolean"],
    Literal["date"],
    Literal["datetime"],
    Literal["duration"],
    Literal["geojson"],
    Literal["geopoint"],
    Literal["integer"],
    Literal["number"],
    Literal["object"],
    Literal["string"],
    Literal["time"],
    Literal["year"],
    Literal["yearmonth"],
]
