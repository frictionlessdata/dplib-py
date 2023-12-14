from __future__ import annotations

from typing import Any, List, Optional, Union

import pydantic

from ... import types
from ...helpers.file import join_basepath
from ...model import Model
from ..contributor import Contributor
from ..dialect import Dialect
from ..license import License
from ..profile import Profile
from ..schema import Schema
from ..source import Source
from .hash import Hash


class Resource(Model):
    basepath: Optional[str] = pydantic.Field(default=None, exclude=True)

    name: Optional[str] = None
    type: Optional[str] = None
    path: Optional[Union[str, List[str]]] = None
    data: Optional[Any] = None
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

    # Getters

    def get_fullpath(self) -> Optional[str]:
        if self.path and isinstance(self.path, str):
            return join_basepath(self.path, self.basepath)

    def get_source(self) -> Optional[Union[str, types.IDict]]:
        return self.data if self.data is not None else self.get_fullpath()

    def get_profile(self) -> Optional[Profile]:
        if self.profile:
            return Profile.from_path(self.profile)

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

    def get_hash(self) -> Optional[Hash]:
        if self.hash:
            return Hash.from_text(self.hash)

    # Methods

    def dereference(self):
        if isinstance(self.dialect, str):
            self.dialect = Dialect.from_path(self.dialect, basepath=self.basepath)
        if isinstance(self.schema, str):
            self.schema = Schema.from_path(self.schema, basepath=self.basepath)  # type: ignore
