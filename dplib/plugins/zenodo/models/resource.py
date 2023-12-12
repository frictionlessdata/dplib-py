from __future__ import annotations

from typing import Optional

from dplib.helpers.resource import slugify_name
from dplib.model import Model
from dplib.models import Resource


class ZenodoResource(Model):
    key: str
    id: Optional[str] = None
    checksum: Optional[str] = None
    ext: Optional[str] = None
    mimetype: Optional[str] = None
    size: Optional[int] = None

    # Converters

    def to_dp(self) -> Resource:
        resource = Resource(path=self.key, name=slugify_name(self.key))

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

        return resource

    @classmethod
    def from_dp(cls, resource: Resource) -> Optional[ZenodoResource]:
        if not resource.path or not isinstance(resource.path, str):
            return

        # Path
        zenodo = ZenodoResource(key=resource.path)

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
