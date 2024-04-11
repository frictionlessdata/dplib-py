from __future__ import annotations

from typing import List, Optional

import pydantic

from ... import types
from ...model import Model


class ForeignKeyReference(Model):
    fields: List[str] = []
    resource: Optional[str] = None

    # Compat

    @pydantic.model_validator(mode="before")
    @classmethod
    def compat(cls, data: types.IData):
        if not isinstance(data, dict):  # type: ignore
            return data

        # foreignKey.reference.fields (standard/v1)
        fields = data.get("fields", None)
        if isinstance(fields, str):
            data["fields"] = [fields]

        return data


class ForeignKey(Model):
    fields: List[str] = []
    reference: ForeignKeyReference = pydantic.Field(default_factory=ForeignKeyReference)

    # Compat

    @pydantic.model_validator(mode="before")
    @classmethod
    def compat(cls, data: types.IData):
        if not isinstance(data, dict):  # type: ignore
            return data

        # foreignKey.fields (standard/v1)
        fields = data.get("fields", None)
        if isinstance(fields, str):
            data["fields"] = [fields]

        return data
