from typing import Any, Optional

from ... import types
from ...model import Model


class Profile(Model):
    jsonSchema: types.IData = {}

    name: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    version: Optional[str] = None

    # Converters

    def to_dict(self):
        data: types.IData = {}
        profile = super().to_dict()
        schema = profile.pop("jsonSchema", {})
        data.update(schema)
        data.update(metadataProfile=profile)
        return data

    @classmethod
    def from_dict(cls, data: types.IData, **kwargs: Any):
        profile = data.pop("metadataProfile", {})
        return cls(jsonSchema=data, **profile)
