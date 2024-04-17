from __future__ import annotations

from typing import Union

import pydantic
from typing_extensions import Annotated

from .datatypes import AnyField, IntegerField, ListField, NumberField, StringField

IField = Annotated[
    Union[AnyField, IntegerField, ListField, NumberField, StringField],
    pydantic.Field(discriminator="type"),
]
