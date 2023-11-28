from __future__ import annotations

from typing import List, Optional

from ...model import Model
from ..contributor import Contributor
from ..license import License
from ..resource import Resource
from ..source import Source


class Package(Model):
    resources: List[Resource] = []

    id: Optional[str] = None
    name: Optional[str] = None
    licenses: Optional[List[License]] = None
    profile: Optional[str] = None

    title: Optional[str] = None
    description: Optional[str] = None
    homepage: Optional[str] = None
    version: Optional[str] = None
    sources: Optional[List[Source]] = None
    contributors: Optional[List[Contributor]] = None
    keywords: Optional[List[str]] = None
    image: Optional[str] = None
    created: Optional[str] = None
