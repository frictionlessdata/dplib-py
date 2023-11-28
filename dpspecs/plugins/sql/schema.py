from typing import List

import sqlalchemy as sa
from sqlalchemy.schema import Table

from ...model import Model
from ...models import ForeignKey, ForeignKeyReference, Schema
from .field import SqlField


class SqlSchema(Model):
    table: Table

    def to_dp(self) -> Schema:
        schema = Schema()

        # Fields
        for column in self.table.columns:
            field = SqlField(column=column).to_dp()
            schema.fields.append(field)

        # Primary key
        for constraint in self.table.constraints:
            if isinstance(constraint, sa.PrimaryKeyConstraint):
                for column in constraint.columns:
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
