from __future__ import annotations

from typing import Any, Optional

import pydantic

from .... import types
from ....system import Model
from ...missingValues import IMissingValues


class BaseField(Model):
    """Base Field"""

    name: Optional[str] = None
    """
    The field descriptor MUST contain a name property.
    """

    # TODO: use proper abstract type (str/Literal string don't work with subclasses)
    type: Optional[Any] = None
    """
    A field type i.e. string, number, etc
    """

    title: Optional[str] = None
    """
    A human readable label or title for the field
    """

    description: Optional[str] = None
    """
    A description for this field e.g. “The recipient of the funds”
    """

    missingValues: IMissingValues = [""]
    """
    A list of field values to consider as null values
    """

    # This method ensures that type is not omitted as defaults in model_dump
    @pydantic.field_serializer("type")
    def serialize_type(self, value: str, info: Any):
        return value

    # Compat

    @pydantic.model_validator(mode="before")
    @classmethod
    def compat(cls, data: types.IDict):
        if not isinstance(data, dict):  # type: ignore
            return data

        # field.format
        format = data.get("format")
        if format:
            if format.startswith("fmt:"):
                data["format"] = format[4:]

        return data
