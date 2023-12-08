from __future__ import annotations

from typing import List, Optional

from ...model import Model


class ForeignKeyReference(Model):
    fields: List[str] = []
    resource: Optional[str] = None
