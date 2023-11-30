from __future__ import annotations

from typing import Dict, List, Optional

import pydantic

from ...model import Model
from ...models import Contributor, Package
from .files import ZenodoFiles
from .metadata import ZenodoMetadata
from .pid import ZenodoPid
from .resource import ZenodoResource
from .subject import ZenodoSubject

# References:
# - https://zenodo.org/records/6533675


class ZenodoPackage(Model):
    files: ZenodoFiles = pydantic.Field(default_factory=ZenodoFiles)
    metadata: ZenodoMetadata = pydantic.Field(default_factory=ZenodoMetadata)

    id: Optional[str] = None
    pids: List[ZenodoPid] = []
    created: Optional[str] = None
    updated: Optional[str] = None
    links: Dict[str, str] = {}

    # Mappers

    def to_dp(self):
        package = Package()

        # General
        if self.metadata.title:
            package.title = self.metadata.title
        if self.metadata.description:
            package.description = self.metadata.description
        if self.metadata.version:
            package.version = self.metadata.version

        # Resources
        for entry in self.files.entries.values():
            resource = entry.to_dp()
            package.resources.append(resource)

        # Keywords
        for subject in self.metadata.subjects:
            package.keywords.append(subject.subject)

        # Contributors
        for creator in self.metadata.creators:
            contributor = Contributor(title=creator.person_or_org.name)
            if creator.person_or_org.type:
                contributor.role = creator.person_or_org.type
            package.contributors.append(contributor)

        return package

    @classmethod
    def from_dp(cls, package: Package) -> ZenodoPackage:
        zenodo = ZenodoPackage()

        # General
        if package.title:
            zenodo.metadata.title = package.title
        if package.description:
            zenodo.metadata.description = package.description
        if package.version:
            zenodo.metadata.version = package.version

        # Resources
        for resource in package.resources:
            entry = ZenodoResource.from_dp(resource)
            if entry:
                zenodo.files.entries[entry.key] = entry

        # keywords
        for keyword in package.keywords:
            subject = ZenodoSubject(subject=keyword)
            zenodo.metadata.subjects.append(subject)

        return zenodo
