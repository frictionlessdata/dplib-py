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
    name: str
    profile: Optional[str] = None

    path: Optional[str] = None
    data: Optional[types.IData] = None

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

    @property
    def parsed_hash(self) -> Optional[ParsedHash]:
        if self.hash:
            parts = self.hash.split(":", maxsplit=1)
            if len(parts) == 1:
                return ParsedHash(type="md5", value=parts[0])
            return ParsedHash(type=parts[0], value=parts[1])
