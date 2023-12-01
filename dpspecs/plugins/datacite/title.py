from __future__ import annotations

from typing import Optional

from ...model import Model


class DataciteTitle(Model):
    title: str
    titleType: Optional[str] = None
    lang: Optional[str] = None
