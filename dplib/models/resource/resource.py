from __future__ import annotations

from typing import Any, List, Optional, Union

import pydantic

from ... import settings, types
from ...helpers.file import join_basepath
from ...helpers.path import assert_safe_path
from ...system import Model
from ..contributor import Contributor
from ..dialect import Dialect
from ..license import License
from ..schema import Schema
from ..source import Source
from .hash import Hash


class Resource(Model):
    """Data Resource model"""

    profile: str = pydantic.Field(
        default=settings.PROFILE_CURRENT_RESOURCE,
        alias="$schema",
    )
    """A profile URL"""

    basepath: Optional[str] = pydantic.Field(default=None, exclude=True)
    """
    Basepath of the resource.
    The data path and dialect/schema will be relative to this basepath.
    """

    name: Optional[str] = None
    """
    A resource MUST contain a name property.
    The name is a simple name or identifier to be used for this resource.
    """

    type: Optional[str] = None
    """
    Type of the resource e.g. "table"
    """

    path: Optional[Union[str, List[str]]] = None
    """
    Path to the data file or to a list of data files
    """

    data: Optional[Any] = None
    """
    Resource data rather than being stored in external files can be shipped inline
    on a Resource using the data property.
    """

    dialect: Optional[Union[Dialect, str]] = None
    """
    A dialect property MAY be provided to specify Table Dialect
    """

    schema: Optional[Union[Schema, str]] = None  # type: ignore
    """
    A schema property MAY be provided to specify Table Schema
    """

    title: Optional[str] = None
    """
    Title or label for the resource.
    """

    description: Optional[str] = None
    """
    Description of the resource.
    """

    format: Optional[str] = None
    """
    Format e.g. ‘csv’, ‘xls’, ‘json’ etc.
    Would be expected to be the standard file extension for this type of resource.
    """

    mediatype: Optional[str] = None
    """
    The mediatype/mimetype of the resource e.g. “text/csv”,
    or “application/vnd.ms-excel”.
    """

    encoding: Optional[str] = None
    """
    Specify the character encoding of the resource’s data file.
    """

    bytes: Optional[int] = None
    """
    Size of the file in bytes.
    """

    hash: Optional[str] = None
    """
    The MD5 hash for this resource.
    Other algorithms can be indicated by prefixing the hash’s value
    with the algorithm name in lower-case.
    """

    sources: List[Source] = []
    """
    The raw sources for this data resource.
    """

    licenses: List[License] = []
    """
    The license(s) under which the resource is provided.
    This property is not legally binding and does not guarantee
    the package is licensed under the terms defined in this property.
    """

    contributors: List[Contributor] = []
    """
    The people or organizations who contributed to this Data Package.
    """

    # Getters

    def get_fullpath(self) -> Optional[str]:
        """Get the full path of the resource

        Returns:
            The full path of the resource
        """
        if self.path and isinstance(self.path, str):
            return join_basepath(self.path, self.basepath)

    def get_source(self) -> Optional[Union[str, types.IDict]]:
        """Get the source of the resource

        Returns:
            Data or full path
        """
        return self.data if self.data is not None else self.get_fullpath()

    def get_dialect(self) -> Optional[Dialect]:
        """Get the resolved dialect of the resource

        Returns:
            The resolved dialect of the resource
        """
        if self.dialect:
            if isinstance(self.dialect, str):
                return Dialect.from_path(self.dialect, basepath=self.basepath)
            return self.dialect

    def get_schema(self) -> Optional[Schema]:
        """Get the resolved schema of the resource

        Returns:
            The resolved schema of the resource
        """
        if self.schema:
            if isinstance(self.schema, str):
                return Schema.from_path(self.schema, basepath=self.basepath)
            return self.schema

    def get_hash(self) -> Optional[Hash]:
        """Get the hash instance of the resource

        Returns:
            The hash instance of the resource
        """
        if self.hash:
            return Hash.from_text(self.hash)

    # Methods

    def dereference(self):
        """Dereference the package
        It will dereference all the resource's dialects and schemas
        """
        if isinstance(self.dialect, str):
            assert_safe_path(self.dialect, basepath=self.basepath)
            self.dialect = Dialect.from_path(self.dialect, basepath=self.basepath)
        if isinstance(self.schema, str):
            assert_safe_path(self.schema, basepath=self.basepath)
            self.schema = Schema.from_path(self.schema, basepath=self.basepath)  # type: ignore

    # Converters

    def to_dict(self):
        data = {"$schema": settings.PROFILE_CURRENT_RESOURCE}
        data.update(super().to_dict())
        return data

    # Compat

    @pydantic.model_validator(mode="before")
    @classmethod
    def compat(cls, data: types.IDict):
        if not isinstance(data, dict):  # type: ignore
            return data

        # resource.url
        if not data.get("path"):
            url = data.pop("url", None)
            if url:
                data["path"] = url

        return data
