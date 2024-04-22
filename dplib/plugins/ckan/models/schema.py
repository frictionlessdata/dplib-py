from __future__ import annotations

from typing import List

from dplib.models import Schema
from dplib.system import Model

from .field import CkanField


class CkanSchema(Model):
    """CKAN Schema model"""

    fields: List[CkanField] = []

    # Converters

    def to_dp(self) -> Schema:
        """Convert to Data Package schema

        Returns:
           Data Resource
        """
        schema = Schema()
        return schema
