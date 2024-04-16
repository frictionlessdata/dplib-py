from __future__ import annotations

from typing import Any, Callable, List

import sqlalchemy as sa
from sqlalchemy.schema import Column, Constraint, Table

from dplib.models import ForeignKey, ForeignKeyReference, Schema
from dplib.system import Model

from . import settings
from .field import SqlField


class SqlSchema(Model, arbitrary_types_allowed=True):
    """SQL Schema model"""

    table: Table

    # Getters

    def get_field_names(self) -> List[str]:
        """Get field names"""
        names: List[str] = []
        for column in self.table.columns:
            names.append(column.name)
        return names

    def get_field_types(self) -> List[Any]:
        """Get field types"""
        types: List[Any] = []
        for column in self.table.columns:
            types.append(type(column.type))
        return types

    # Converters

    def to_dp(self, *, with_metadata: bool = False) -> Schema:
        """Convert to Table Schema

        Returns:
            Table Schema
        """
        schema = Schema()

        # Fields
        for column in self.table.columns:
            if with_metadata and column.name in settings.METADATA_IDENTIFIERS:
                continue
            field = SqlField(column=column).to_dp()
            schema.fields.append(field)

        # Primary key
        for constraint in self.table.constraints:
            if isinstance(constraint, sa.PrimaryKeyConstraint):
                for column in constraint.columns:
                    if with_metadata and column.name in settings.METADATA_IDENTIFIERS:
                        continue
                    schema.primaryKey.append(str(column.name))

        # Foreign keys
        for constraint in self.table.constraints:
            if isinstance(constraint, sa.ForeignKeyConstraint):
                resource = ""
                own_fields: List[str] = []
                foreign_fields: List[str] = []
                for element in constraint.elements:
                    own_fields.append(str(element.parent.name))
                    if element.column.table.name != self.table.name:
                        resource = str(element.column.table.name)
                    foreign_fields.append(str(element.column.name))
                ref = ForeignKeyReference(resource=resource, fields=foreign_fields)
                fk = ForeignKey(fields=own_fields, reference=ref)
                schema.foreignKeys.append(fk)

        return schema

    @classmethod
    def from_dp(
        cls,
        schema: Schema,
        *,
        table_name: str,
        dialect: str = settings.DEFAULT_DIALECT,
        with_metadata: bool = False,
    ) -> SqlSchema:
        """Create SQL Schema from Table Schema

        Parameters:
            schema: Table Schema
            table_name: SQL table name
            dialect: SQL dialect
            with_metadata: Include metadata columns

        Returns:
            SQL Schema
        """
        columns: List[Column[Any]] = []
        constraints: List[Constraint] = []

        # Fields
        if with_metadata:
            columns.append(
                sa.Column(
                    settings.ROW_NUMBER_IDENTIFIER,
                    sa.Integer,
                    primary_key=True,
                    autoincrement=False,
                )
            )
            columns.append(sa.Column(settings.ROW_VALID_IDENTIFIER, sa.Boolean))
        for field in schema.fields:
            sql_field = SqlField.from_dp(field, table_name=table_name, dialect=dialect)
            columns.append(sql_field.column)

        # Primary key
        if schema.primaryKey:
            Class = sa.UniqueConstraint if with_metadata else sa.PrimaryKeyConstraint
            if not with_metadata:
                constraint = Class(*schema.primaryKey)
                constraints.append(constraint)

        # Foreign keys
        for fk in schema.foreignKeys:
            prefix: Callable[[str], str] = lambda field: ".".join([foreign_table, field])
            foreign_table = fk.reference.resource or table_name
            foreign_fields = list(map(prefix, fk.reference.fields))
            constraint = sa.ForeignKeyConstraint(fk.fields, foreign_fields)
            constraints.append(constraint)

        table = sa.Table(table_name, sa.MetaData(), *(columns + constraints))
        return SqlSchema(table=table)
