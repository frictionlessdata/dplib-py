from __future__ import annotations

from typing import List, Optional

from dplib.model import Model

from .creator import ZenodoCreator
from .subject import ZenodoSubject


class ZenodoMetadata(Model):
    creators: List[ZenodoCreator] = []
    description: Optional[str] = None
    publication_date: Optional[str] = None
    publisher: Optional[str] = None
    subjects: List[ZenodoSubject] = []
    title: Optional[str] = None
    version: Optional[str] = None
