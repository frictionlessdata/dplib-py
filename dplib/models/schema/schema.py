from __future__ import annotations

from typing import List, Optional

from ...model import Model
from ..profile import Profile
from .field import Field
from .foreignKey import ForeignKey


class Schema(Model):
    """Schema model"""

    profile: Optional[str] = None

    fields: List[Field] = []
    """List of fields"""

    missingValues: List[str] = [""]
    primaryKey: List[str] = []
    foreignKeys: List[ForeignKey] = []

    # Getters

    def get_profile(self) -> Optional[Profile]:
        if self.profile:
            return Profile.from_path(self.profile)

    def get_field(self, *, name: Optional[str] = None) -> Optional[Field]:
        for field in self.fields:
            if name and field.name == name:
                return field

    # Setters

    def add_field(self, field: Field) -> None:
        self.fields.append(field)
