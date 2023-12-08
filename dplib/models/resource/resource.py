from __future__ import annotations

from typing import List, Optional

from ... import types
from ...model import Model
from ..contributor import Contributor
from ..dialect import Dialect
from ..license import License
from ..schema import Schema
from ..source import Source
from .parsedHash import ParsedHash


class Resource(Model):
    name: Optional[str] = None
    profile: Optional[str] = None

    path: Optional[str] = None
    data: Optional[types.IDict] = None

    dialect: Optional[Dialect] = None
    schema: Optional[Schema] = None  # type: ignore

    title: Optional[str] = None
    description: Optional[str] = None
    format: Optional[str] = None
    mediatype: Optional[str] = None
    encoding: Optional[str] = None
    bytes: Optional[int] = None
    hash: Optional[str] = None
    sources: List[Source] = []
    licenses: List[License] = []
    contributors: List[Contributor] = []

    @property
    def parsed_hash(self) -> Optional[ParsedHash]:
        if self.hash:
            return ParsedHash.from_hash(self.hash)
