from __future__ import annotations

from typing import List

from ...model import Model
from .creator import ZenodoCreator
from .subject import ZenodoSubject


class ZenodoMetadata(Model):
    creators: List[ZenodoCreator]
    description: str
    publication_date: str
    publisher: str
    subjects: List[ZenodoSubject]
    title: str
    version: str
