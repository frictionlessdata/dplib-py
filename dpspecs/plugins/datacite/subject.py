from __future__ import annotations

from typing import Optional

from ...model import Model


class DataciteSubject(Model):
    subject: str
    lang: Optional[str] = None
