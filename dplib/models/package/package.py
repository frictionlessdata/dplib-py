from __future__ import annotations

from typing import List, Optional

import pydantic

from ... import settings
from ...system import Model
from ..contributor import Contributor
from ..license import License
from ..resource import Resource
from ..source import Source


class Package(Model):
    """Data Package model"""

    profile: str = pydantic.Field(
        default=settings.PROFILE_CURRENT_PACKAGE,
        alias="$schema",
    )
    """A profile URL"""

    basepath: Optional[str] = pydantic.Field(default=None, exclude=True)
    """
    Basepath of the package.
    All the resources are relative to this path.
    """

    resources: List[Resource] = []
    """
    List of resources
    """

    id: Optional[str] = None
    """
    A property reserved for globally unique identifiers.
    Examples of identifiers that are unique include UUIDs and DOIs.
    """

    name: Optional[str] = None
    """
    A short url-usable (and preferably human-readable) name of the package.
    This MUST be lower-case and contain only alphanumeric characters
    along with ”.”, ”_” or ”-” characters.
    """

    title: Optional[str] = None
    """
    A string providing a title or one sentence description for this package
    """

    description: Optional[str] = None
    """
    A description of the package. The description MUST be markdown formatted —
    this also allows for simple plain text as plain text is itself valid markdown.
    """

    homepage: Optional[str] = None
    """
    A URL for the home on the web that is related to this data package.
    """

    version: Optional[str] = None
    """
    A version string identifying the version of the package.
    It should conform to the Semantic Versioning requirements
    """

    licenses: List[License] = []
    """
    The license(s) under which the package is provided.
    This property is not legally binding and does not guarantee
    the package is licensed under the terms defined in this property.
    """

    sources: List[Source] = []
    """
    The raw sources for this data package.
    """

    contributors: List[Contributor] = []
    """
    The people or organizations who contributed to this Data Package.
    """

    keywords: List[str] = []
    """
    An Array of string keywords to assist users searching for the package in catalogs.
    """

    image: Optional[str] = None
    """
    An image to use for this data package.
    For example, when showing the package in a listing.
    """

    created: Optional[str] = None
    """
    The datetime on which this was created.
    """

    def model_post_init(self, _):
        for resource in self.resources:
            resource.basepath = self.basepath

    # Getters

    def get_resource(
        self, *, name: Optional[str] = None, path: Optional[str] = None
    ) -> Optional[Resource]:
        """Get a resource by name or path

        Parameters:
            name: The name of the resource
            path: The path of the resource

        Returns:
            The resource if found
        """
        for resource in self.resources:
            if name and resource.name == name:
                return resource
            if path and resource.path == path:
                return resource

    # Setters

    def add_resource(self, resource: Resource) -> None:
        """Add a resource to the package

        Parameters:
            resource: The resource to add
        """
        resource.basepath = self.basepath
        self.resources.append(resource)

    # Methods

    def dereference(self):
        """Dereference the package
        It will dereference all the resource's dialects and schemas in the package.
        """
        for resource in self.resources:
            resource.dereference()

    # Converters

    def to_dict(self):
        data = {"$schema": settings.PROFILE_CURRENT_PACKAGE}
        data.update(super().to_dict())
        return data
