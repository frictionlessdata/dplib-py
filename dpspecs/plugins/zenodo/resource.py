from __future__ import annotations

from ...model import Model


class ZenodoResource(Model):
    checksum: str
    ext: str
    id: str
    key: str
    mimetype: str
    size: int
