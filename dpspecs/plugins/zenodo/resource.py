from __future__ import annotations

from ...helpers.resource import path_to_name
from ...model import Model
from ...models import Resource


class ZenodoResource(Model):
    checksum: str
    ext: str
    id: str
    key: str
    mimetype: str
    size: int

    def to_dp(self) -> Resource:
        resource = Resource(path=self.key, name=path_to_name(self.key))
        resource.format = self.ext.lower()
        resource.mimetype = self.mimetype
        resource.bytes = self.size
        resource.hash = self.checksum.replace("md5:", "")
        return resource
