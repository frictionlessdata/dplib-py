from __future__ import annotations

from typing import List, Optional

from ...model import Model
from ..contributor import Contributor
from ..dialect import Dialect
from ..license import License
from ..schema import Schema
from ..source import Source


class Resource(Model):
    name: str
    path: str

    profile: Optional[str] = None

    dialect: Optional[Dialect] = None
    schema: Optional[Schema] = None  # type: ignore

    title: Optional[str] = None
    description: Optional[str] = None
    format: Optional[str] = None
    mediatype: Optional[str] = None
    encoding: Optional[str] = None
    bytes: Optional[int] = None
    hash: Optional[str] = None
    sources: Optional[List[Source]] = None
    licenses: Optional[List[License]] = None
    contributors: Optional[List[Contributor]] = None