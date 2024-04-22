from __future__ import annotations

from typing import Any, Literal, Optional, Union

import pydantic

from ..constraints import StringConstraints
from .base import BaseField

IStringFormat = Union[
    Literal["binary"],
    Literal["default"],
    Literal["email"],
    Literal["uri"],
    Literal["uuid"],
]


class StringField(BaseField):
    """The field contains strings, that is, sequences of characters."""

    type: Literal["string"] = "string"
    format: Optional[IStringFormat] = None
    constraints: StringConstraints = pydantic.Field(default_factory=StringConstraints)

    @pydantic.field_serializer("type")
    def serialize_type(self, value: str, info: Any):
        return value
