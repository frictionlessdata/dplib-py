from __future__ import annotations

from typing import Any, Dict, List, Literal, Optional, Union

import pydantic
from typing_extensions import Annotated

from ...model import Model


class BaseField(Model):
    name: str
    type: str
    title: Optional[str] = None
    description: Optional[str] = None
    format: Optional[str] = None
    missingValues: Optional[List[str]] = None


class AnyField(BaseField):
    type: Literal["any"] = "any"


class ArrayField(BaseField):
    type: Literal["array"] = "array"
    # support json/csv format
    arrayItem: Optional[Dict[str, Any]] = None


class BooleanField(BaseField):
    type: Literal["boolean"] = "boolean"
    trueValues: Optional[List[str]] = None
    falseValues: Optional[List[str]] = None


class DateField(BaseField):
    type: Literal["date"] = "date"


class DatetimeField(BaseField):
    type: Literal["datetime"] = "datetime"


class DurationField(BaseField):
    type: Literal["duration"] = "duration"


class GeojsonField(BaseField):
    type: Literal["geojson"] = "geojson"


class GeopointField(BaseField):
    type: Literal["geopoint"] = "geopoint"


class IntegerField(BaseField):
    type: Literal["integer"] = "integer"
    bareNumber: Optional[bool] = None
    groupChar: Optional[str] = None


class NumberField(BaseField):
    type: Literal["number"] = "number"
    bareNumber: Optional[bool] = None
    groupChar: Optional[str] = None
    decimalChar: Optional[str] = None


class ObjectField(BaseField):
    type: Literal["object"] = "object"


class StringField(BaseField):
    type: Literal["string"] = "string"


class TimeField(BaseField):
    type: Literal["time"] = "time"


class YearField(BaseField):
    type: Literal["year"] = "year"


class YearmonthField(BaseField):
    type: Literal["yearmonth"] = "yearmonth"


Field = Annotated[
    Union[
        AnyField,
        ArrayField,
        BooleanField,
        DateField,
        DatetimeField,
        DurationField,
        GeojsonField,
        GeopointField,
        IntegerField,
        NumberField,
        ObjectField,
        StringField,
        TimeField,
        YearField,
        YearmonthField,
    ],
    pydantic.Field(discriminator="type"),
]
