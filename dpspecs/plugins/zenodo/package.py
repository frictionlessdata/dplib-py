from __future__ import annotations

from typing import Dict, List, Optional

from ...model import Model
from ...models import Package
from .files import ZenodoFiles
from .metadata import ZenodoMetadata
from .pid import ZenodoPid

# References:
# - https://zenodo.org/records/6533675


class ZenodoPackage(Model):
    files: ZenodoFiles

    metadata: ZenodoMetadata
    pids: List[ZenodoPid] = []

    id: Optional[str] = None
    created: Optional[str] = None
    updated: Optional[str] = None
    links: Dict[str, str] = {}

    def to_dp(self):
        resources = self.files.to_dp()
        return Package(resources=resources)

    @classmethod
    def from_dp(cls, package: Package) -> ZenodoPackage:
        files = ZenodoFiles.from_dp(package.resources)
        return ZenodoPackage(files=files)
