from __future__ import annotations

from typing import List, Optional

import pydantic

from ...model import Model


class ForeignKeyReference(Model):
    fields: List[str] = []
    resource: Optional[str] = None


class ForeignKey(Model):
    fields: List[str] = []
    reference: ForeignKeyReference = pydantic.Field(default_factory=ForeignKeyReference)
