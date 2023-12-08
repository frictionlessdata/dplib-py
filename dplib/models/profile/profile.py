from typing import List, Optional

from ... import types
from ...model import Model
from .constraint import Constraint


class Profile(Model):
    jsonSchema: types.IDict = {}

    title: Optional[str] = None
    description: Optional[str] = None
    constraints: List[Constraint] = []

    # Converters

    def to_dict(self):
        data = super().to_dict()
        schema = data.pop("jsonSchema", {})
        data.update(schema)
        return data

    @classmethod
    def from_dict(cls, data: types.IDict):
        title = data.pop("title", None)
        description = data.pop("description", None)
        constraints = data.pop("constraints", [])
        return cls(
            title=title,
            description=description,
            constraints=constraints,
            jsonSchema=data,
        )
