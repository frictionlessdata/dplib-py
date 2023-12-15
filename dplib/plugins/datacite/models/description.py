from __future__ import annotations

from typing import Optional

from dplib.model import Model


class DataciteDescription(Model):
    description: str
    descriptionType: str
    lang: Optional[str] = None
