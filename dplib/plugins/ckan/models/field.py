from __future__ import annotations

from typing import Optional

from dplib import models
from dplib.system import Model


class CkanFieldInfo(Model):
    """CKAN FieldInfo model"""

    label: str
    notes: str
    type_override: str


class CkanField(Model):
    """CKAN Field model"""

    id: str
    type: str
    info: Optional[CkanFieldInfo] = None

    def to_dp(self) -> models.IField:
        """Convert to Table Schema Field

        Returns:
            Table Schema Field
        """
        # Type
        Field = models.Field
        if self.type == "text":
            Field = models.StringField
        elif self.type == "int":
            Field = models.IntegerField
        elif self.type == "numeric":
            Field = models.NumberField
        elif self.type == "bool":
            Field = models.BooleanField
        elif self.type == "date":
            Field = models.DateField
        elif self.type == "time":
            Field = models.TimeField
        elif self.type == "timestamp":
            Field = models.DatetimeField
        elif self.type == "json":
            Field = models.ObjectField

        # Name
        field = Field(name=self.id)

        if self.info:
            # Title
            if self.info.label:
                field.title = self.info.label

            # Description
            if self.info.notes:
                field.description = self.info.notes

        return field
