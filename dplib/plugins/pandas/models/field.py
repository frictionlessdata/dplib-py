from __future__ import annotations

import datetime
from typing import Any, Optional

import isodate  # type: ignore
import numpy as np
import pandas as pd
import pandas.core.dtypes.api as pdc

from dplib import models
from dplib.error import Error
from dplib.system import Model


class PandasField(Model, arbitrary_types_allowed=True):
    """Pandas Field model"""

    name: str
    dtype: Any
    dvalue: Optional[Any] = None

    # Converters

    def to_dp(self) -> models.IField:
        """Convert to Table Schema Field

        Returns:
            Table Schema Field
        """

        # Type
        Field = models.Field
        if pdc.is_bool_dtype(self.dtype):  # type: ignore
            Field = models.BooleanField
        elif pdc.is_datetime64_any_dtype(self.dtype):  # type: ignore
            Field = models.DatetimeField
        elif pdc.is_integer_dtype(self.dtype):  # type: ignore
            Field = models.IntegerField
        elif pdc.is_numeric_dtype(self.dtype):  # type: ignore
            Field = models.NumberField
        elif self.dvalue is not None:
            if isinstance(self.dvalue, (list, tuple)):  # type: ignore
                Field = models.ArrayField
            elif isinstance(self.dvalue, datetime.datetime):
                Field = models.DatetimeField
            elif isinstance(self.dvalue, datetime.date):
                Field = models.DateField
            elif isinstance(self.dvalue, isodate.Duration):  # type: ignore
                Field = models.DurationField
            elif isinstance(self.dvalue, dict):
                Field = models.ObjectField
            elif isinstance(self.dvalue, str):
                Field = models.StringField
            elif isinstance(self.dvalue, datetime.time):
                Field = models.TimeField

        # Name
        field = Field(name=self.name)

        return field

    @classmethod
    def from_dp(cls, field: models.IField) -> PandasField:
        """Create Pandas Field from Table Schema Field

        Parameters:
            field: Table Schema Field

        Returns:
            Pandas Field
        """
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
