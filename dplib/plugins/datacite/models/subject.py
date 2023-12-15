from __future__ import annotations

from typing import Optional

from dplib.model import Model


class DataciteSubject(Model):
    subject: str
    subjectScheme: Optional[str] = None
    schemeUri: Optional[str] = None
    lang: Optional[str] = None
