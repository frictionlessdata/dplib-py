from __future__ import annotations

from typing import List, Optional

from ...model import Model
from ..profile import Profile
from .field import Field
from .foreignKey import ForeignKey


class Schema(Model):
    """Table Schema model"""

    profile: Optional[str] = None
    """
    An URL identifying the profile of this descriptor as per the profiles specification.
    """

    title: Optional[str] = None
    """
    A string providing a title or one sentence description for this schema
    """

    description: Optional[str] = None
    """
    A description of the schema. The description MUST be markdown formatted —
    this also allows for simple plain text as plain text is itself valid markdown.
    """

    fields: List[Field] = []
    """
    List of fields in the table schema
    """

    missingValues: List[str] = [""]
    """
    A list of field values to consider as null values
    """

    primaryKey: List[str] = []
    """
    A primary key is a field or set of fields that uniquely identifies
    each row in the table.
    """

    foreignKeys: List[ForeignKey] = []
    """
    A foreign key is a reference where values in a field (or fields)
    on the table (‘resource’ in data package terminology) described by this Table Schema
    connect to values a field (or fields) on this or a separate table (resource).
    """

    # Getters

    def get_profile(self) -> Optional[Profile]:
        """Get the resovled profile of the schema

        Returns:
            The resolved profile of the schema
        """
        if self.profile:
            return Profile.from_path(self.profile)

    def get_field(self, *, name: Optional[str] = None) -> Optional[Field]:
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
            types.append(field.type)
        return types

    # Setters

    def add_field(self, field: Field):
        """Add a field to the schema

        Parameters:
            field: The field to add
        """
        self.fields.append(field)
