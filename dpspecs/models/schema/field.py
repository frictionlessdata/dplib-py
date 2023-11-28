from __future__ import annotations

from typing import Any, Dict, List, Literal, Optional, Union

import pydantic
from pydantic import Field
from typing_extensions import Annotated

from ...model import Model
from . import constraints


class BaseField(Model):
    name: str
    type: str
    title: Optional[str] = None
    description: Optional[str] = None
    format: Optional[str] = None
    missingValues: Optional[List[str]] = None


class AnyField(BaseField):
    type: Literal["any"] = "any"
    constraints = constraints.BaseConstraints()


class ArrayField(BaseField):
    type: Literal["array"] = "array"
    # support json/csv format
    arrayItem: Optional[Dict[str, Any]] = None
    constraints = constraints.CollectionConstraints()


class BooleanField(BaseField):
    type: Literal["boolean"] = "boolean"
    trueValues: Optional[List[str]] = None
    falseValues: Optional[List[str]] = None
    constraints = constraints.BaseConstraints()


class DateField(BaseField):
    type: Literal["date"] = "date"
    constraints = constraints.ValueConstraints()


class DatetimeField(BaseField):
    type: Literal["datetime"] = "datetime"
    constraints = constraints.ValueConstraints()


class DurationField(BaseField):
    type: Literal["duration"] = "duration"
    constraints = constraints.BaseConstraints()


class GeojsonField(BaseField):
    type: Literal["geojson"] = "geojson"
    constraints = constraints.BaseConstraints()


class GeopointField(BaseField):
    type: Literal["geopoint"] = "geopoint"
    constraints = constraints.BaseConstraints()


class IntegerField(BaseField):
    type: Literal["integer"] = "integer"
    bareNumber: Optional[bool] = None
    groupChar: Optional[str] = None
    constraints = constraints.ValueConstraints()


class NumberField(BaseField):
    type: Literal["number"] = "number"
    bareNumber: Optional[bool] = None
    groupChar: Optional[str] = None
    decimalChar: Optional[str] = None
    constraints = constraints.ValueConstraints()


class ObjectField(BaseField):
    type: Literal["object"] = "object"
    constraints = constraints.CollectionConstraints()


class StringField(BaseField):
    type: Literal["string"] = "string"
    constraints: constraints.StringConstraints = Field(
        default_factory=constraints.StringConstraints
    )


class TimeField(BaseField):
    type: Literal["time"] = "time"
    constraints = constraints.ValueConstraints()


class YearField(BaseField):
    type: Literal["year"] = "year"
    constraints = constraints.ValueConstraints()


class YearmonthField(BaseField):
    type: Literal["yearmonth"] = "yearmonth"
    constraints = constraints.ValueConstraints()


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
