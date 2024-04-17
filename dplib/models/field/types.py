from __future__ import annotations

from typing import Union

import pydantic
from typing_extensions import Annotated

from . import datatypes
from .field import Field

IField = Annotated[
    Union[
        Field,
        datatypes.AnyField,
        datatypes.ArrayField,
        datatypes.BooleanField,
        datatypes.DateField,
        datatypes.DatetimeField,
        datatypes.DurationField,
        datatypes.GeojsonField,
        datatypes.GeopointField,
        datatypes.IntegerField,
        datatypes.ListField,
        datatypes.NumberField,
        datatypes.ObjectField,
        datatypes.StringField,
        datatypes.TimeField,
        datatypes.YearField,
        datatypes.YearmonthField,
    ],
    pydantic.Field(discriminator="type"),
]
