from __future__ import annotations

import datetime
from typing import Any, Optional

import isodate
import pandas as pd
import pandas.core.dtypes.api as pdc
from typing_extensions import Self

from ...model import Model
from ...models import Field


class PandasField(Model, arbitrary_types_allowed=True):
    name: str
    dtype: Any
    dvalue: Optional[Any] = None

    def to_dp(self) -> Field:
        field = Field(name=self.name)

        # Pandas types
        if pdc.is_bool_dtype(self.dtype):  # type: ignore
            field.type = "boolean"
        elif pdc.is_datetime64_any_dtype(dtype):  # type: ignore
            field.type = "datetime"
        elif pdc.is_integer_dtype(dtype):  # type: ignore
            field.type = "integer"
        elif pdc.is_numeric_dtype(dtype):  # type: ignore
            field.type = "number"

        # Python types
        if self.dvalue is not None:
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
        dtype = cls.__write_convert_type(field.type)
        return cls(name=field.name, dtype=dtype)
