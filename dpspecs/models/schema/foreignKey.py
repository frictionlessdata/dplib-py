from __future__ import annotations

from typing import List

from ...model import Model
from .foreignKeyReference import ForeignKeyReference


class ForeignKey(Model):
    fields: List[str]
    reference: ForeignKeyReference
