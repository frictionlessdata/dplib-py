from __future__ import annotations

from typing import Any, Dict, List, Optional

import pydantic

from ...model import Model
from .constraints import Constraints
from .fieldType import FieldType


class Field(Model):
    """Table Schema Field model"""

    name: Optional[str] = None
    """
    The field descriptor MUST contain a name property.
    """

    type: FieldType = "any"
    """
    A field’s type property is a string indicating the type of this field.
    """

    format: Optional[str] = None
    """
    A field’s format property is a string, indicating a format for the field type.
    """

    title: Optional[str] = None
    """
    A human readable label or title for the field
    """

    description: Optional[str] = None
    """
    A description for this field e.g. “The recipient of the funds”
    """

    missingValues: List[str] = [""]
    """
    A list of field values to consider as null values
    """

    constraints: Constraints = pydantic.Field(default_factory=Constraints)
    """
    The constraints property on Table Schema Fields can be used by consumers
    to list constraints for validating field values.
    """

    # Array

    arrayItem: Optional[Dict[str, Any]] = None
    """
    Field descriptor for items for array fields
    """

    # Boolean

    trueValues: Optional[List[str]] = None
    """
    Values to be interpreted as “true” for boolean fields
    """

    falseValues: Optional[List[str]] = None
    """
    Values to be interpreted as “false” for boolean fields
    """

    # Integer/Number

    bareNumber: Optional[bool] = None
    """
    If false leading and trailing non numbers will be removed for integer/number fields
    """

    # Number

    groupChar: Optional[str] = None
    """
    String whose value is used to group digits for number fields
    """

    decimalChar: Optional[str] = None
    """
    String whose value is used to represent a decimal point for number fields
    """
