from __future__ import annotations

from typing import Any, Dict

import polars as pl
from typing_extensions import Self

from ...model import Model
from ...models import Schema
from .field import PolarsField


class PolarsSchema(Model, arbitrary_types_allowed=True):
    df: pl.DataFrame

    def to_dp(self) -> Schema:
        schema = Schema()

        # Fields
        for name, dtype in self.df.schema.items():
            field = PolarsField(name=name, dtype=dtype).to_dp()
            schema.fields.append(field)

        return schema

    @classmethod
    def from_dp(cls, schema: Schema) -> Self:
        columns: Dict[str, pd.Series] = {}

        # Fields
        for field in schema.fields:
            pandas_field = PandasField.from_dp(field)
            columns[pandas_field.name] = pd.Series(dtype=pandas_field.dtype)

        # Primary key
        index = schema.primaryKey

        return PandasSchema(df=pd.DataFrame(columns, index=index))
