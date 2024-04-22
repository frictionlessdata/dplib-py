from __future__ import annotations

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
    info: CkanFieldInfo

    def to_dp(self) -> models.IField:
        """Convert to Table Schema Field

        Returns:
            Table Schema Field
        """
        # Type
        Field = models.Field
        if self.type == "text":
            Field = models.StringField
        if self.type == "int":
            Field = models.IntegerField
        if self.type == "float":
            Field = models.NumberField
        if self.type == "bool":
            Field = models.BooleanField
        if self.type == "date":
            Field = models.DateField
        if self.type == "time":
            Field = models.TimeField
        if self.type == "timestamp":
            Field = models.DatetimeField
        if self.type == "json":
            Field = models.ObjectField

        # Name
        field = Field(name=self.id)

        # Title
        if self.info.label:
            field.title = self.info.label

        # Description
        if self.info.notes:
            field.description = self.info.notes

        return field
