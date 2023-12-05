from __future__ import annotations

from typing import List

from ...model import Model


class ForeignKeyReference(Model):
    fields: List[str]
    resource: str
