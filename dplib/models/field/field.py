from __future__ import annotations

from typing import List, Optional

import pydantic

from ... import types
from ...model import Model
from .constraints import Constraints
from .types import IFieldType, IItemType


class Field(Model):
    """Table Schema Field model"""

    name: Optional[str] = None
    """
    The field descriptor MUST contain a name property.
    """

    type: IFieldType = "any"
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

    groupChar: Optional[str] = None
    """
    String whose value is used to group digits for integer/number fields
    """

    # List

    delimiter: Optional[str] = None
    """
    Specifies the character sequence which separates lexically represented list items.
    """

    itemType: Optional[IItemType] = None
    """
    Specifies the list item type in terms of existent Table Schema types.
    """

    # Number

    decimalChar: Optional[str] = None
    """
    String whose value is used to represent a decimal point for number fields
    """

    # Compat

    @pydantic.model_validator(mode="before")
    @classmethod
    def compat(cls, data: types.IData):
        if not isinstance(data, dict):  # type: ignore
            return data

        # field.format
        format = data.get("format")
        if format:
            if format.startswith("fmt:"):
                data["format"] = format[4:]

        return data
