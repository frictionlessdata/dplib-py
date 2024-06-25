from __future__ import annotations

from typing import Literal, Optional, Union

import pydantic

from ..categories import ICategories
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

    categories: Optional[ICategories] = None
    """
    Property to restrict the field to a finite set of possible values
    """

    categoriesOrdered: bool = False
    """
    When categoriesOrdered is true, implementations SHOULD regard the order of
    appearance of the values in the categories property as their natural order.
    """
