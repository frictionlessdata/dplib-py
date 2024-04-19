from __future__ import annotations

import os
from typing import Optional

from dplib.helpers.resource import slugify_name
from dplib.models import Resource
from dplib.system import Model


class CkanResource(Model):
    """CKAN Resource model"""

    url: str
    name: str
    created: Optional[str] = None
    description: Optional[str] = None
    format: Optional[str] = None  # NOTE: uppercased
    hash: Optional[str] = None
    id: Optional[str] = None
    last_modified: Optional[str] = None
    metadata_modified: Optional[str] = None
    mimetype: Optional[str] = None
    size: Optional[int] = None

    # Converters

    def to_dp(self) -> Resource:
        """Convert to Data Package resource

        Returns:
           Data Resource
        """
        # Path/Name
        resource = Resource(path=self.url, name=slugify_name(self.name))

        # Description
        if self.description:
            resource.description = self.description

        # Format
        if self.format:
            resource.format = self.format.lower()

        # Mediatype
        if self.mimetype:
            resource.mediatype = self.mimetype

        # Size
        if self.size:
            resource.bytes = self.size

        # Custom
        if self.id:
            resource.custom["ckan:id"] = self.id

        return resource

    @classmethod
    def from_dp(cls, resource: Resource) -> Optional[CkanResource]:
        """Create CKAN Resource from Data Resource

        Parameters:
            resource: Data Resource

        Returns:
            CKAN Resource
        """
        if not resource.path or not isinstance(resource.path, str):
            return

        # Path/Name
        ckan = CkanResource(url=resource.path, name=os.path.basename(resource.path))

        # Description
        if resource.description:
            ckan.description = resource.description

        # Format
        if resource.format:
            ckan.format = resource.format.upper()

        # Mediatype
        if resource.mediatype:
            ckan.mimetype = resource.mediatype

        # Bytes
        if resource.bytes:
            ckan.size = resource.bytes

        return ckan
