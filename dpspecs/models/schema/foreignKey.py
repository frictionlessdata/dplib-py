from __future__ import annotations

from typing import List, Optional

from ...model import Model
from .foreignKeyReference import ForeignKeyReference


class ForeignKey(Model):
    fields: List[str]
    reference: Optional[ForeignKeyReference] = None
