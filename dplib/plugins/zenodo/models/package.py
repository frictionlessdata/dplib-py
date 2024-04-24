from __future__ import annotations

from typing import Dict, Optional

import pydantic

from dplib.models import Contributor, License, Package
from dplib.system import Model

from .contributor import ZenodoContributor, ZenodoContributorAffiliation
from .files import ZenodoFiles
from .metadata import ZenodoMetadata
from .pid import ZenodoPid
from .resource import ZenodoResource
from .right import ZenodoRight
from .subject import ZenodoSubject

# References:
# - https://zenodo.org/records/6533675


class ZenodoPackage(Model):
    """Zenodo Package model"""

    files: ZenodoFiles = pydantic.Field(default_factory=ZenodoFiles)
    metadata: ZenodoMetadata = pydantic.Field(default_factory=ZenodoMetadata)

    id: Optional[str] = None
    pids: Dict[str, ZenodoPid] = {}
    created: Optional[str] = None
    updated: Optional[str] = None
    links: Dict[str, str] = {}

    # Converters

    def to_dp(self) -> Package:
        """Convert to Data Package

        Returns:
           Data Package
        """
        package = Package()

        # Id
        if self.links.get("doi"):
            package.id = self.links.get("doi")

        # Name
        if self.id:
            package.name = self.id

        # Title
        if self.metadata.title:
            package.title = self.metadata.title

        # Description
        if self.metadata.description:
            package.description = self.metadata.description

        # Version
        if self.metadata.version:
            package.version = self.metadata.version

        # Created
        if self.created:
            package.created = self.created

        # Homepage
        if self.links.get("self_html"):
            package.homepage = self.links.get("self_html")

        # Keywords
        for subject in self.metadata.subjects:
            package.keywords.append(subject.subject)

        # Resources
        for entry in self.files.entries.values():
            if self.id:
                resource = entry.to_dp(package_id=self.id)
                package.resources.append(resource)

        # Licenses
        for right in self.metadata.rights:
            if right.id:
                license = License(
                    name=right.id,
                    title=right.title.en,
                    path=right.link or right.props.url,
                )
                package.licenses.append(license)

        # Contributors
        for type, items in [
            ("creator", self.metadata.creators),
            ("contributor", self.metadata.contributors),
        ]:
            for item in items:
                if item.person_or_org.name:
                    contributor = Contributor(
                        title=item.person_or_org.name,
                        givenName=item.person_or_org.given_name,
                        familyName=item.person_or_org.family_name,
                        roles=[item.role.id or type],
                    )
                    if item.affiliations:
                        contributor.organization = item.affiliations[0].name
                    package.contributors.append(contributor)

        # Custom
        if self.id:
            package.custom["zenodo:id"] = self.id

        return package

    @classmethod
    def from_dp(cls, package: Package) -> ZenodoPackage:
        """Create a Zenodo Package from Data Package

        Parameters:
            package: Data Package

        Returns:
            Zenodo Package
        """
        zenodo = ZenodoPackage()

        # Title
        if package.title:
            zenodo.metadata.title = package.title

        # Description
        if package.description:
            zenodo.metadata.description = package.description

        # Version
        if package.version:
            zenodo.metadata.version = package.version

        # Keywords
        for keyword in package.keywords:
            subject = ZenodoSubject(subject=keyword)
            zenodo.metadata.subjects.append(subject)

        # Resources
        for resource in package.resources:
            entry = ZenodoResource.from_dp(resource)
            if entry:
                zenodo.files.entries[entry.key] = entry

        # Licenses
        for license in package.licenses:
            right = ZenodoRight()
            right.id = license.name
            right.link = license.path
            right.title.en = license.title
            zenodo.metadata.rights.append(right)

        # Contributors
        for contributor in package.contributors:
            item = ZenodoContributor()
            item.person_or_org.name = contributor.title
            item.person_or_org.given_name = contributor.givenName
            item.person_or_org.family_name = contributor.familyName
            if contributor.roles:
                item.role.id = contributor.roles[0]
            if contributor.organization:
                affiliation = ZenodoContributorAffiliation(name=contributor.organization)
                item.affiliations.append(affiliation)
            if contributor.roles and contributor.roles[0] == "creator":
                zenodo.metadata.creators.append(item)
            else:
                zenodo.metadata.contributors.append(item)

        return zenodo
