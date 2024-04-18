from __future__ import annotations

from typing import Literal, Optional, Union

import pydantic

from ..constraints import CollectionConstraints
from .base import BaseField

IItemType = Union[
    Literal["boolean"],
    Literal["date"],
    Literal["datetime"],
    Literal["integer"],
    Literal["number"],
    Literal["string"],
    Literal["time"],
]


class ListField(BaseField):
    """The field contains data that is an ordered
    one-level depth collection of primitive values with a fixed item type.
    """

    type: Literal["list"] = "list"
    format: Optional[Literal["default"]] = None
    constraints: CollectionConstraints = pydantic.Field(
        default_factory=CollectionConstraints
    )

    delimiter: Optional[str] = None
    """
    Specifies the character sequence which separates lexically represented list items.
    """

    itemType: Optional[IItemType] = None
    """
    Specifies the list item type in terms of existent Table Schema types.
    """
