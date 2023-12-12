from __future__ import annotations

from typing import Optional

from dplib.helpers.resource import slugify_name
from dplib.model import Model
from dplib.models import Resource


class CkanResource(Model):
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
        resource = Resource(path=self.name, name=slugify_name(self.name))

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
        if not resource.path or not isinstance(resource.path, str):
            return

        # Path
        ckan = CkanResource(name=resource.path)

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
