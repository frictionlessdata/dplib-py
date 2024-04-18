from __future__ import annotations

import random
from string import ascii_lowercase as letters
from typing import Any, List, Optional

import sqlalchemy as sa
from sqlalchemy.dialects import mysql as ml
from sqlalchemy.dialects import postgresql as pg
from sqlalchemy.dialects import registry
from sqlalchemy.schema import Column

from dplib import models
from dplib.system import Model

from . import settings


class SqlField(Model, arbitrary_types_allowed=True):
    """SQL Field model"""

    column: Column[Any]

    # Converters

    def to_dp(self) -> models.IField:
        """Convert to Table Schema Field

        Returns:
            Table Schema Field
        """
        # Type
        Field = models.Field
        if isinstance(self.column.type, ARRAY_TYPES):
            Field = models.ArrayField
        elif isinstance(self.column.type, BOOLEAN_TYPES):
            Field = models.BooleanField
        elif isinstance(self.column.type, DATE_TYPES):
            Field = models.DateField
        elif isinstance(self.column.type, DATETIME_TYPES):
            Field = models.DatetimeField
        elif isinstance(self.column.type, INTEGER_TYPES):
            Field = models.IntegerField
        elif isinstance(self.column.type, NUMBER_TYPES):
            Field = models.NumberField
        elif isinstance(self.column.type, OBJECT_TYPES):
            Field = models.ObjectField
        elif isinstance(self.column.type, STRING_TYPES):
            Field = models.StringField
        elif isinstance(self.column.type, TIME_TYPES):
            Field = models.TimeField

        # Name
        field = Field(name=self.column.name)

        # Description
        if self.column.comment:
            field.description = self.column.comment

        # Constraints
        if not self.column.nullable:
            field.constraints.required = True
        if isinstance(self.column.type, sa.Enum):
            if self.column.enums:
                field.constraints.enum = self.column.enums
        if isinstance(field, models.StringField):
            if isinstance(self.column.type, (sa.CHAR, sa.VARCHAR)):
                if self.column.type.length:
                    field.constraints.maxLength = self.column.type.length
            if isinstance(self.column.type, sa.CHAR):
                if self.column.type.length:
                    field.constraints.minLength = self.column.type.length

        return field

    @classmethod
    def from_dp(
        cls,
        field: models.IField,
        *,
        dialect: str = settings.DEFAULT_DIALECT,
        table_name: Optional[str] = None,
    ) -> SqlField:
        """Create SQL Field from Table Schema Field

        Parameters:
            field: Table Schema Field
            dialect: SQL dialect
            table_name: SQL table name

        Returns:
            SQL Field
        """
        Check = sa.CheckConstraint
        checks: List[sa.CheckConstraint] = []
        comment = field.description
        dialect_obj = registry.load(dialect)()
        nullable = not field.constraints.required
        quoted_name = dialect_obj.identifier_preparer.quote(field.name)

        # Type
        column_type = sa.Text
        if field.type == "any":
            column_type = sa.Text
        elif field.type == "boolean":
            column_type = sa.Boolean
        elif field.type == "date":
            column_type = sa.Date
        elif field.type == "datetime":
            column_type = sa.DateTime
        elif field.type == "integer":
            column_type = sa.Integer
        elif field.type == "number":
            column_type = sa.Float
        elif field.type == "string":
            column_type = sa.Text
        elif field.type == "time":
            column_type = sa.Time
        elif field.type == "year":
            column_type = sa.Integer
        if dialect_obj.name == "postgresql":
            if field.type == "array":
                column_type = pg.JSONB
            elif field.type == "geojson":
                column_type = pg.JSONB
            elif field.type == "object":
                column_type = pg.JSONB
            elif field.type == "number":
                column_type = sa.Numeric

        # Unique contstraint
        unique = field.constraints.unique
        if dialect_obj.name == "mysql":
            # MySQL requires keys to have an explicit maximum length
            # https://stackoverflow.com/questions/1827063/mysql-error-key-specification-without-a-key-length
            unique = unique and column_type is not sa.Text

        # Length contraints
        if field.type == "string":
            min = field.constraints.minLength
            max = field.constraints.maxLength
            if min is not None and max is not None and min == max:
                column_type = sa.CHAR(max)
            if max is not None:
                if column_type is sa.Text:
                    column_type = sa.VARCHAR(length=max)
                if dialect_obj.name == "sqlite":
                    checks.append(Check("LENGTH(%s) <= %s" % (quoted_name, max)))
            if min is not None:
                if not isinstance(column_type, sa.CHAR) or dialect_obj.name == "sqlite":
                    checks.append(Check("LENGTH(%s) >= %s" % (quoted_name, min)))

        # Limit contstraints
        if isinstance(field, (models.IntegerField, models.NumberField)):
            min = field.constraints.minimum
            max = field.constraints.maximum
            if min is not None:
                checks.append(Check("%s >= %s" % (quoted_name, min)))
            if max is not None:
                checks.append(Check("%s <= %s" % (quoted_name, max)))

        # Pattern constraint
        if field.type == "string":
            val = field.constraints.pattern
            if val is not None:
                if dialect_obj.name == "postgresql":
                    checks.append(Check("%s ~ '%s'" % (quoted_name, val)))
                elif dialect_obj.name != "duckdb":
                    check = Check("%s REGEXP '%s'" % (quoted_name, val))
                    checks.append(check)

        # Enum constraint
        if field.type == "string":
            val = field.constraints.enum
            if val is not None:
                # NOTE: https://github.com/frictionlessdata/frictionless-py/issues/778
                if not table_name:
                    table_name = "".join(random.choice(letters) for _ in range(8))
                enum_name = "%s_%s_enum" % (table_name, field.name)
                quoted_enum_name = dialect_obj.identifier_preparer.quote(enum_name)
                column_type = sa.Enum(*val, name=quoted_enum_name)

        # TODO: shall it use "autoincrement=False"
        # https://github.com/Mause/duckdb_engine/issues/595#issuecomment-1495408566
        column_args = [field.name, column_type] + checks
        column_kwargs = {"nullable": nullable, "unique": unique, "comment": comment}
        column = sa.Column(*column_args, **column_kwargs)  # type: ignore
        return SqlField(column=column)


ARRAY_TYPES = (pg.ARRAY,)
BOOLEAN_TYPES = (sa.Boolean,)
DATE_TYPES = (sa.Date,)
DATETIME_TYPES = (sa.DateTime,)
INTEGER_TYPES = (sa.Integer,)
NUMBER_TYPES = (sa.Float, sa.Numeric)  # type: ignore
STRING_TYPES = (ml.BIT, ml.VARBINARY, ml.VARCHAR, pg.UUID, sa.Text, sa.VARCHAR)  # type: ignore
OBJECT_TYPES = (pg.JSONB, pg.JSON)
TIME_TYPES = (sa.Time,)
