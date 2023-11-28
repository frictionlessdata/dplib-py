from typing import Any, List

import sqlalchemy as sa
from sqlalchemy.dialects import mysql as ml
from sqlalchemy.dialects import postgresql as pg
from sqlalchemy.dialects import registry
from sqlalchemy.schema import Column
from typing_extensions import Self

from ...model import Model
from ...models.schema import field as fields


class SqlField(Model):
    column: Column[Any]

    # Mappers

    @classmethod
    def from_dp(cls, field: fields.Field, *, dialect: str = "postgresql") -> Self:
        Check = sa.CheckConstraint
        checks: List[Check] = []
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
            min_length = field.constraints.minLength
            max_length = field.constraints.maxLength

            if (
                min_length is not None
                and max_length is not None
                and min_length == max_length
            ):
                column_type = sa.CHAR(max_length)
            if max_length is not None:
                if column_type is sa.Text:
                    column_type = sa.VARCHAR(length=max_length)
                if dialect_obj.name == "sqlite":
                    checks.append(Check("LENGTH(%s) <= %s" % (quoted_name, max_length)))
            if min_length is not None:
                if not isinstance(column_type, sa.CHAR) or dialect_obj.name == "sqlite":
                    checks.append(Check("LENGTH(%s) >= %s" % (quoted_name, min_length)))

        # Value contstraints
        if field.type == "integer":
            minimum = field.constraints.minimum
            if field.constraints.minimum is not None:
                checks.append(
                    Check("%s >= %s" % (quoted_name, field.constraints.minimum))
                )

        # Others contstraints
        for const, value in field.constraints.items():
            if const == "minimum":
                checks.append(Check("%s >= %s" % (quoted_name, value)))
            elif const == "maximum":
                checks.append(Check("%s <= %s" % (quoted_name, value)))
            elif const == "pattern":
                if self.dialect.name == "postgresql":
                    checks.append(Check("%s ~ '%s'" % (quoted_name, value)))
                elif self.dialect.name != "duckdb":
                    check = Check("%s REGEXP '%s'" % (quoted_name, value))
                    checks.append(check)
            elif const == "enum":
                # NOTE: https://github.com/frictionlessdata/frictionless-py/issues/778
                if field.type == "string":
                    enum_name = "%s_%s_enum" % (table_name, field.name)
                    column_type = sa.Enum(*value, name=enum_name)

        # Create column
        column_args = [field.name, column_type] + checks  # type: ignore
        # TODO: shall it use "autoincrement=False"
        # https://github.com/Mause/duckdb_engine/issues/595#issuecomment-1495408566
        column_kwargs = {"nullable": nullable, "unique": unique}
        if field.description:
            column_kwargs["comment"] = field.description
        column = sa.Column(*column_args, **column_kwargs)

        return column

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
