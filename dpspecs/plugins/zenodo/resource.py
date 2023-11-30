from __future__ import annotations

from typing import Optional

from ...helpers.resource import path_to_name
from ...model import Model
from ...models import Resource


class ZenodoResource(Model):
    key: str
    id: Optional[str] = None
    checksum: Optional[str] = None
    ext: Optional[str] = None
    mimetype: Optional[str] = None
    size: Optional[int] = None

    # Mappers

    def to_dp(self) -> Resource:
        resource = Resource(path=self.key, name=path_to_name(self.key))

        # General
        if self.ext:
            resource.format = self.ext.lower()
        if self.mimetype:
            resource.mediatype = self.mimetype
        if self.size:
            resource.bytes = self.size
        if self.checksum:
            resource.hash = self.checksum.replace("md5:", "")

        return resource

    @classmethod
    def from_dp(cls, resource: Resource) -> Optional[ZenodoResource]:
        if not resource.path:
            return
        zenodo = ZenodoResource(key=resource.path)

        # General
        if resource.format:
            zenodo.ext = resource.format
        if resource.mediatype:
            zenodo.mimetype = resource.mediatype
        if resource.bytes:
            zenodo.size = resource.bytes
        if resource.parsed_hash:
            if resource.parsed_hash.type == "md5":
                zenodo.checksum = resource.parsed_hash.full_hash

        return zenodo
