from __future__ import annotations

from typing import List, Optional

from ...model import Model
from .field import Field
from .foreignKey import ForeignKey


class Schema(Model):
    """Schema model"""

    fields: List[Field]
    """List of fields"""

    missingValues: Optional[List[str]] = None
    primaryKey: Optional[List[str]] = None
    foreignKeys: Optional[List[ForeignKey]] = None
