from __future__ import annotations

from typing import Any

import polars as pl

from dplib.error import Error
from dplib.model import Model
from dplib.models import Field


class PolarsField(Model, arbitrary_types_allowed=True):
    name: str
    dtype: Any
    #  dtype: pl.PolarsDataType

    # Converters

    def to_dp(self) -> Field:
        field = Field(name=self.name)

        if self.dtype in ARRAY_TYPES:
            field.type = "array"
        elif self.dtype in BOOLEAN_TYPES:
            field.type = "boolean"
        elif self.dtype in DATE_TYPES:
            field.type = "date"
        elif self.dtype in DATETIME_TYPES:
            field.type = "datetime"
        elif self.dtype in DURATION_TYPES:
            field.type = "duration"
        elif self.dtype in INTEGER_TYPES:
            field.type = "integer"
        elif self.dtype in NUMBER_TYPES:
            field.type = "number"
        elif self.dtype in OBJECT_TYPES:
            field.type = "object"
        elif self.dtype in STRING_TYPES:
            field.type = "string"
        elif self.dtype in TIME_TYPES:
            field.type = "time"

        return field

    @classmethod
    def from_dp(cls, field: Field) -> PolarsField:
        if not field.name:
            raise Error(f"Field name is required to convert to polars: {field}")

        # Type
        dtype = pl.Utf8
        if field.type == "array":
            dtype = pl.List
        elif field.type == "boolean":
            dtype = pl.Boolean
        elif field.type == "date":
            dtype = pl.Date
        elif field.type == "datetime":
            dtype = pl.Datetime
        elif field.type == "duration":
            dtype = pl.Duration
        elif field.type == "geojson":
            dtype = pl.Struct
        elif field.type == "geopoint":
            dtype = pl.List
        elif field.type == "integer":
            dtype = pl.Int64
        elif field.type == "number":
            dtype = pl.Decimal
        elif field.type == "object":
            dtype = pl.Struct
        elif field.type == "string":
            dtype = pl.Utf8
        elif field.type == "time":
            dtype = pl.Time
        elif field.type == "year":
            dtype = pl.Int8
        elif field.type == "yearmonth":
            dtype = pl.List

        return PolarsField(name=field.name, dtype=dtype)


ARRAY_TYPES = (pl.Array, pl.List)
BOOLEAN_TYPES = (pl.Boolean,)
DATE_TYPES = (pl.Date,)
DATETIME_TYPES = (pl.Datetime,)
DURATION_TYPES = (pl.Duration,)
INTEGER_TYPES = (
    pl.Int8,
    pl.Int16,
    pl.Int32,
    pl.Int64,
    pl.UInt8,
    pl.UInt16,
    pl.UInt32,
    pl.UInt64,
)
NUMBER_TYPES = (pl.Float32, pl.Float64, pl.Decimal)
STRING_TYPES = (pl.Utf8, pl.Categorical)
OBJECT_TYPES = (pl.Struct,)
TIME_TYPES = (pl.Time,)
