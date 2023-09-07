from __future__ import annotations

from typing import Any, Dict, List, Literal, Optional

from .base import Model


class Schema(Model):
    """Schema model"""

    name: Optional[str] = None
    type: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None

    fields: List[Field]
    """List of fields"""

    missingValues: Optional[List[str]] = None
    primaryKey: Optional[List[str]] = None
    foreignKeys: Optional[List[ForeignKey]] = None


class Field(Model):
    name: str
    type: str
    title: Optional[str] = None
    description: Optional[str] = None
    format: Optional[str] = None
    missingValues: Optional[List[str]] = None


class AnyField(Field):
    type: Literal["any"]


class ArrayField(Field):
    type: Literal["array"]
    # support json/csv format
    arrayItem: Optional[Dict[str, Any]] = None


class BooleanField(Field):
    type: Literal["boolean"]
    trueValues: Optional[List[str]] = None
    falseValues: Optional[List[str]] = None


class DateField(Field):
    type: Literal["date"]


class DatetimeField(Field):
    type: Literal["datetime"]


class DurationField(Field):
    type: Literal["duration"]


class GeojsonField(Field):
    type: Literal["geojson"]


class GeopointField(Field):
    type: Literal["geopoint"]


class IntegerField(Field):
    type: Literal["integer"]
    bareNumber: Optional[bool] = None
    groupChar: Optional[str] = None


class NumberField(Field):
    type: Literal["number"]
    bareNumber: Optional[bool] = None
    groupChar: Optional[str] = None
    decimalChar: Optional[str] = None


class ObjectField(Field):
    type: Literal["object"]


class StringField(Field):
    type: Literal["string"]


class TimeField(Field):
    type: Literal["time"]


class YearField(Field):
    type: Literal["year"]


class YearmonthField(Field):
    type: Literal["yearmonth"]


class ForeignKeyReference(Model):
    fields: List[str]
    resource: str


class ForeignKey(Model):
    fields: List[str]
    reference: Optional[ForeignKeyReference] = None
