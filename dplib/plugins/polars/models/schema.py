from __future__ import annotations

from typing import Dict, List

import polars as pl

from dplib.models import Schema
from dplib.system import Model

from .field import PolarsField


class PolarsSchema(Model, arbitrary_types_allowed=True):
    """Polars Schema model"""

    df: pl.DataFrame

    # Getters

    def get_field_names(self) -> List[str]:
        """Get field names"""
        return list(self.df.schema.keys())

    def get_field_types(self) -> List[pl.PolarsDataType]:
        """Get field types"""
        return list(self.df.schema.values())

    # Converters

    def to_dp(self) -> Schema:
        """Convert to Table Schema

        Returns:
            Table Schema
        """
        schema = Schema()

        # Fields
        for name, dtype in self.df.schema.items():
            field = PolarsField(name=name, dtype=dtype).to_dp()
            schema.fields.append(field)

        return schema

    @classmethod
    def from_dp(cls, schema: Schema) -> PolarsSchema:
        """Create Polars Schema from Table Schema

        Parameters:
            schema: Table Schema

        Returns:
            Polars Schema
        """
        columns: Dict[str, pl.PolarsDataType] = {}

        # Fields
        for field in schema.fields:
            polars_field = PolarsField.from_dp(field)
            columns[polars_field.name] = polars_field.dtype

        return PolarsSchema(df=pl.DataFrame(schema=columns))
