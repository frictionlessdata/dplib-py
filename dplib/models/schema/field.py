from __future__ import annotations

from typing import Any, Dict, List, Optional

import pydantic

from ...model import Model
from .constraints import Constraints
from .fieldType import FieldType


# TODO: consider getting back to discriminated unions
class Field(Model):
    name: Optional[str] = None
    type: FieldType = "any"
    title: Optional[str] = None
    description: Optional[str] = None
    format: Optional[str] = None
    missingValues: List[str] = [""]
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
