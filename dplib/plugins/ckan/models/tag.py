from __future__ import annotations

from typing import Optional

from dplib.model import Model


class CkanTag(Model):
    name: str
    id: Optional[str] = None
    display_name: Optional[str] = None
