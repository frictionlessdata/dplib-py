from __future__ import annotations

from typing import List, Optional

import pydantic

from ... import settings, types
from ...system import Model

#  from ..contributor import Contributor
from ..field import IField
from ..missingValues import IMissingValues
from .foreignKey import ForeignKey
from .types import IFieldsMatch


class Schema(Model):
    """Table Schema model"""

    profile: str = pydantic.Field(
        default=settings.PROFILE_CURRENT_SCHEMA,
        alias="$schema",
    )
    """A profile URL"""

    #  name: Optional[str] = None
    """
    A simple name or identifier as for Data Package
    """

    #  title: Optional[str] = None
    """
    A string providing a title or one sentence description for this schema
    """

    #  description: Optional[str] = None
    """
    A description of the schema. The description MUST be markdown formatted —
    this also allows for simple plain text as plain text is itself valid markdown.
    """

    #  homepage: Optional[str] = None
    """
    A URL for the home on the web that is related to this data package.
    """

    #  keywords: List[str] = []
    """
    The `keywords` property is a list of short keywords related to the schema.
    """

    #  examples: List[dict[str, str]] = []
    """
    The `examples` property contains links to example data resources.
    """

    #  version: Optional[str] = None
    """
    The `version` property stores the version of the schema
    """

    #  contributors: List[Contributor] = []
    """
    The people or organizations who contributed to this Table Schema.
    """

    fields: List[IField] = []
    """
    List of fields in the table schema
    """

    fieldsMatch: Optional[IFieldsMatch] = "exact"
    """
    The way Table Schema fields are mapped onto the data source fields
    are defined by the fieldsMatch property.
    """

    missingValues: IMissingValues = [""]
    """
    A list of field values to consider as null values
    """

    primaryKey: List[str] = []
    """
    A primary key is a field or set of fields that uniquely identifies
    each row in the table.
    """

    uniqueKeys: List[List[str]] = []
    """
    A unique key is a field or a set of fields that are required
    to have unique logical values in each row in the table.
    """

    foreignKeys: List[ForeignKey] = []
    """
    A foreign key is a reference where values in a field (or fields)
    on the table (‘resource’ in data package terminology) described by this Table Schema
    connect to values a field (or fields) on this or a separate table (resource).
    """

    # Getters

    def get_field(self, *, name: Optional[str] = None) -> Optional[IField]:
        """Get a field by name

        Parameters:
            name: The name of the field to get

        Returns:
            The field with the given name if found
        """
        for field in self.fields:
            if name and field.name == name:
                return field

    def get_field_names(self) -> List[str]:
        """Get the names of the fields in the schema

        Returns:
            The names of the fields in the schema
        """
        names: List[str] = []
        for field in self.fields:
            names.append(field.name or "")
        return names

    def get_field_types(self) -> List[str]:
        """Get the types of the fields in the schema

        Returns:
            The types of the fields in the schema
        """
        types: List[str] = []
        for field in self.fields:
            types.append(field.type or "any")
        return types

    # Setters

    def add_field(self, field: IField):
        """Add a field to the schema

        Parameters:
            field: The field to add
        """
        self.fields.append(field)

    # Converters

    def to_dict(self):
        data = {"$schema": settings.PROFILE_CURRENT_SCHEMA}
        data.update(super().to_dict())
        return data

    # Compat

    @pydantic.model_validator(mode="before")
    @classmethod
    def compat(cls, data: types.IDict):
        if not isinstance(data, dict):  # type: ignore
            return data

        # schema.primaryKey
        primaryKey = data.get("primaryKey", None)
        if isinstance(primaryKey, str):
            data["primaryKey"] = [primaryKey]

        return data
