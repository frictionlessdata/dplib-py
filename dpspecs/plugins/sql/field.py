from typing import Any, Self

import sqlalchemy as sa
from sqlalchemy.dialects import mysql as ml
from sqlalchemy.dialects import postgresql as pg
from sqlalchemy.schema import Column

from ...model import Model
from ...models.schema import field as fields


class SqlField(Model):
    column: Column[Any]

    # Mappers

    @classmethod
    def from_dp(cls, field: fields.Field) -> Self:
        pass

    def to_dp(self) -> fields.Field:
        # Type/name
        Field = fields.AnyField
        if isinstance(self.column.type, ARRAY_TYPES):
            Field = fields.ArrayField
        elif isinstance(self.column.type, BOOLEAN_TYPES):
            Field = fields.BooleanField
        elif isinstance(self.column.type, DATE_TYPES):
            Field = fields.DateField
        elif isinstance(self.column.type, DATETIME_TYPES):
            Field = fields.DatetimeField
        elif isinstance(self.column.type, INTEGER_TYPES):
            Field = fields.IntegerField
        elif isinstance(self.column.type, NUMBER_TYPES):
            Field = fields.NumberField
        elif isinstance(self.column.type, OBJECT_TYPES):
            Field = fields.ObjectField
        elif isinstance(self.column.type, TIME_TYPES):
            Field = fields.TimeField
        field = Field(name=self.column.name)

        # Description
        if self.column.comment:
            field.description = self.column.comment

        # Constraints
        if not self.column.nullable:
            field.constraints.required = True
        if isinstance(self.column.type, (sa.CHAR, sa.VARCHAR)):
            if self.column.type.length:
                field.constraints.maxLength = self.column.type.length
        if isinstance(self.column.type, sa.CHAR):
            if self.column.type.length:
                field.constraints.minLength = self.column.type.length
        if isinstance(self.column.type, sa.Enum):
            if self.column.enums:
                field.constraints.enum = self.column.enums

        return field


ARRAY_TYPES = (pg.ARRAY,)
BOOLEAN_TYPES = (sa.Boolean,)
DATE_TYPES = (sa.Date,)
DATETIME_TYPES = (sa.DateTime,)
INTEGER_TYPES = (sa.Integer,)
NUMBER_TYPES = (sa.Float, sa.Numeric)  # type: ignore
STRING_TYPES = (ml.BIT, ml.VARBINARY, ml.VARCHAR, pg.UUID, sa.Text, sa.VARCHAR)  # type: ignore
OBJECT_TYPES = (pg.JSONB, pg.JSON)
TIME_TYPES = (sa.Time,)
