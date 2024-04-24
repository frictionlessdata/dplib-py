from __future__ import annotations

from typing import List, Optional

from dplib.system import Model

from .contributor import ZenodoContributor
from .subject import ZenodoSubject


class ZenodoMetadata(Model):
    creators: List[ZenodoContributor] = []
    contributors: List[ZenodoContributor] = []
    description: Optional[str] = None
    publication_date: Optional[str] = None
    publisher: Optional[str] = None
    subjects: List[ZenodoSubject] = []
    title: Optional[str] = None
    version: Optional[str] = None
