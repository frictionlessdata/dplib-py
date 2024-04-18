from __future__ import annotations

from typing import List, Optional

import pydantic

from .... import types
from ....system import Model


class BaseField(Model):
    """Base Field"""

    name: Optional[str] = None
    """
    The field descriptor MUST contain a name property.
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
