from __future__ import annotations

import datetime
from typing import Any, Optional

import isodate  # type: ignore
import numpy as np
import pandas as pd
import pandas.core.dtypes.api as pdc

from dplib.error import Error
from dplib.model import Model
from dplib.models import Field


class PandasField(Model, arbitrary_types_allowed=True):
    name: str
    dtype: Any
    dvalue: Optional[Any] = None

    # Converters

    def to_dp(self) -> Field:
        field = Field(name=self.name)

        # Type
        if pdc.is_bool_dtype(self.dtype):  # type: ignore
            field.type = "boolean"
        elif pdc.is_datetime64_any_dtype(self.dtype):  # type: ignore
            field.type = "datetime"
        elif pdc.is_integer_dtype(self.dtype):  # type: ignore
            field.type = "integer"
        elif pdc.is_numeric_dtype(self.dtype):  # type: ignore
            field.type = "number"
        elif self.dvalue is not None:
            if isinstance(self.dvalue, (list, tuple)):  # type: ignore
                field.type = "array"
            elif isinstance(self.dvalue, datetime.datetime):
                field.type = "datetime"
            elif isinstance(self.dvalue, datetime.date):
                field.type = "date"
            elif isinstance(self.dvalue, isodate.Duration):  # type: ignore
                field.type = "duration"
            elif isinstance(self.dvalue, dict):
                field.type = "object"
            elif isinstance(self.dvalue, str):
                field.type = "string"
            elif isinstance(self.dvalue, datetime.time):
                field.type = "time"

        return field

    @classmethod
    def from_dp(cls, field: Field) -> PandasField:
        if not field.name:
            raise Error(f"Field name is required to convert to pandas: {field}")

        # Type
        dtype = np.dtype("O")
        if field.type == "array":
            dtype = np.dtype(list)  # type: ignore
        elif field.type == "boolean":
            dtype = np.dtype(bool)
        elif field.type == "datetime":
            dtype = pd.DatetimeTZDtype(tz="UTC")
        elif field.type == "integer":
            dtype = np.dtype(int)
        elif field.type == "geojson":
            dtype = np.dtype(dict)
        elif field.type == "number":
            dtype = np.dtype(float)
        elif field.type == "object":
            dtype = np.dtype(dict)
        elif field.type == "string":
            dtype = np.dtype(str)
        elif field.type == "year":
            dtype = np.dtype(int)

        return PandasField(name=field.name, dtype=dtype)
