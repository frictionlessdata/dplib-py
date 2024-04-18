from __future__ import annotations

from typing import Any

import polars as pl

from dplib import models
from dplib.error import Error
from dplib.system import Model


class PolarsField(Model, arbitrary_types_allowed=True):
    """Polars Field model"""

    name: str
    dtype: Any
    #  dtype: pl.PolarsDataType

    # Converters

    def to_dp(self) -> models.IField:
        """Convert to Table Schema Field

        Returns:
            Table Schema Field
        """

        # Type
        Field = models.Field
        if self.dtype in ARRAY_TYPES:
            Field = models.ArrayField
        elif self.dtype in BOOLEAN_TYPES:
            Field = models.BooleanField
        elif self.dtype in DATE_TYPES:
            Field = models.DateField
        elif self.dtype in DATETIME_TYPES:
            Field = models.DatetimeField
        elif self.dtype in DURATION_TYPES:
            Field = models.DurationField
        elif self.dtype in INTEGER_TYPES:
            Field = models.IntegerField
        elif self.dtype in NUMBER_TYPES:
            Field = models.NumberField
        elif self.dtype in OBJECT_TYPES:
            Field = models.ObjectField
        elif self.dtype in STRING_TYPES:
            Field = models.StringField
        elif self.dtype in TIME_TYPES:
            Field = models.TimeField

        # Name
        field = Field(name=self.name)

        return field

    @classmethod
    def from_dp(cls, field: models.IField) -> PolarsField:
        """Create Polars Field from Table Schema Field

        Parameters:
            field: Table Schema Field

        Returns:
            Polars Field
        """
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
