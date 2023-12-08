from __future__ import annotations

from typing import List, Optional, Union

import pydantic

from ... import types
from ...model import Model
from ..contributor import Contributor
from ..dialect import Dialect
from ..license import License
from ..schema import Schema
from ..source import Source
from .hash import Hash


class Resource(Model):
    name: Optional[str] = None
    type: Optional[str] = None
    path: Optional[str] = None
    data: Optional[types.IDict] = None
    profile: Optional[str] = None
    dialect: Optional[Union[Dialect, str]] = None
    schema: Optional[Union[Schema, str]] = None  # type: ignore

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

    basepath: Optional[str] = pydantic.Field(default=None, exclude=True)

    # Getters

    def get_hash(self) -> Optional[Hash]:
        if self.hash:
            return Hash.from_text(self.hash)

    def get_dialect(self) -> Optional[Dialect]:
        if self.dialect:
            if isinstance(self.dialect, str):
                return Dialect.from_path(self.dialect, basepath=self.basepath)
            return self.dialect

    def get_schema(self) -> Optional[Schema]:
        if self.schema:
            if isinstance(self.schema, str):
                return Schema.from_path(self.schema, basepath=self.basepath)
            return self.schema
