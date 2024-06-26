from __future__ import annotations

from typing import Literal, Optional

import pydantic

from ..categories import ICategories
from ..constraints import ValueConstraints
from .base import BaseField


class IntegerField(BaseField):
    """The field contains integers - that is whole numbers."""

    type: Literal["integer"] = "integer"
    format: Optional[Literal["default"]] = None
    constraints: ValueConstraints[int] = pydantic.Field(default_factory=ValueConstraints)

    categories: Optional[ICategories] = None
    """
    Property to restrict the field to a finite set of possible values
    """

    categoriesOrdered: bool = False
    """
    When categoriesOrdered is true, implementations SHOULD regard the order of
    appearance of the values in the categories property as their natural order.
    """

    groupChar: Optional[str] = None
    """
    String whose value is used to group digits for integer/number fields
    """

    bareNumber: bool = True
    """
    If false leading and trailing non numbers will be removed for integer/number fields
    """
