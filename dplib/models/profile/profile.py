from typing import Any, List, Optional

from ... import types
from ...model import Model
from .rule import Rule


class Profile(Model):
    jsonSchema: types.IDict = {}

    name: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    version: Optional[str] = None
    rules: List[Rule] = []

    # Converters

    def to_dict(self):
        data: types.IDict = {}
        profile = super().to_dict()
        schema = profile.pop("jsonSchema", {})
        data.update(schema)
        data.update(metadataProfile=profile)
        return data

    @classmethod
    def from_dict(cls, data: types.IDict, **kwargs: Any):
        profile = data.pop("metadataProfile", {})
        return cls(jsonSchema=data, **profile)
