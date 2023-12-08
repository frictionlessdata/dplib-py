from __future__ import annotations

from typing import List

from ...model import Model
from .field import Field
from .foreignKey import ForeignKey


class Schema(Model):
    """Schema model"""

    fields: List[Field] = []
    """List of fields"""

    missingValues: List[str] = []
    primaryKey: List[str] = []
    foreignKeys: List[ForeignKey] = []
