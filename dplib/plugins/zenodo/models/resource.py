from __future__ import annotations

import os
from typing import Optional

from dplib.helpers.resource import slugify_name
from dplib.models import Resource
from dplib.system import Model


class ZenodoResource(Model):
    """Zenodo Resource model"""

    key: str
    id: Optional[str] = None
    checksum: Optional[str] = None
    ext: Optional[str] = None
    mimetype: Optional[str] = None
    size: Optional[int] = None

    # Converters

    def to_dp(self, *, package_id: str) -> Resource:
        """Convert to Data Package resource

        Returns:
           Data Resource
        """
        resource = Resource(
            path=f"https://zenodo.org/records/{package_id}/files/{self.key}",
            name=slugify_name(self.key),
        )

        # Format
        if self.ext:
            resource.format = self.ext.lower()

        # Mediatype
        if self.mimetype:
            resource.mediatype = self.mimetype

        # Bytes
        if self.size:
            resource.bytes = self.size

        # Hash
        if self.checksum:
            resource.hash = self.checksum.replace("md5:", "")

        # Custom
        if self.id:
            resource.custom["zenodo:id"] = self.id

        return resource

    @classmethod
    def from_dp(cls, resource: Resource) -> Optional[ZenodoResource]:
        """Create Zenodo Resource from Data Resource

        Parameters:
            resource: Data Resource

        Returns:
            Zenodo Resource
        """
        if not resource.path or not isinstance(resource.path, str):
            return

        # Path
        zenodo = ZenodoResource(key=os.path.basename(resource.path))

        # Format
        if resource.format:
            zenodo.ext = resource.format

        # Mediatype
        if resource.mediatype:
            zenodo.mimetype = resource.mediatype

        # Bytes
        if resource.bytes:
            zenodo.size = resource.bytes

        # Hash
        hash = resource.get_hash()
        if hash:
            if hash.type == "md5":
                zenodo.checksum = hash.long

        return zenodo
