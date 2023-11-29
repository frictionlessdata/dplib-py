from __future__ import annotations

from typing import Any, Callable, List

import pandas as pd
from typing_extensions import Self

from ...model import Model
from ...models import Schema
from .field import PandasField


class PandasSchema(Model, arbitrary_types_allowed=True):
    df: pd.DataFrame

    def to_dp(self) -> Schema:
        schema = Schema()

        # Primary key
        for index, name in enumerate(self.df.index.names):  # type: ignore
            dtype = self.df.index.get_level_values(index).dtype  # type: ignore
            field = PandasField(name=name, dtype=dtype).to_dp()
            field.constraints.required = True
            schema.fields.append(field)
            schema.primaryKey.append(name)

        # Fields
        for name, dtype in self.df.dtypes.items():  # type: ignore
            dvalue: Any = self.df[name].iloc[0] if len(self.df) else None  # type: ignore
            field = PandasField(name=str(name), dtype=dtype, dvalue=dvalue).to_dp()
            schema.fields.append(field)

        return schema
