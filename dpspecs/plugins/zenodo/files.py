from __future__ import annotations

from typing import Dict, List, Optional

from ...model import Model
from ...models import Resource
from .resource import ZenodoResource


class ZenodoFiles(Model):
    count: int
    entries: Dict[str, ZenodoResource]
    total_bytes: Optional[int] = None

    # Mappers

    def to_dp(self) -> List[Resource]:
        resources: List[Resource] = []
        for entry in self.entries.values():
            resource = entry.to_dp()
            resources.append(resource)
        return resources

    @classmethod
    def from_dp(cls, resources: List[Resource]) -> ZenodoFiles:
        entries: Dict[str, ZenodoResource] = {}
        for resource in resources:
            entry = ZenodoResource.from_dp(resource)
            if entry:
                entries[entry.key] = entry
        return ZenodoFiles(count=len(entries), entries=entries)
