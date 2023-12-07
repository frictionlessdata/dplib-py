from __future__ import annotations

from typing import List, Optional

from dplib.model import Model
from dplib.models import Contributor, License, Package

from .organization import CkanOrganization
from .resource import CkanResource
from .tag import CkanTag

# References:
# - https://demo.ckan.org/api/3/action/package_show?id=sample-dataset-1


class CkanPackage(Model):
    resources: List[CkanResource] = []

    organization: Optional[CkanOrganization] = None
    tags: List[CkanTag] = []

    id: Optional[str] = None
    name: Optional[str] = None
    title: Optional[str] = None
    notes: Optional[str] = None
    version: Optional[str] = None
    notes: Optional[str] = None
    license_id: Optional[str] = None
    license_title: Optional[str] = None
    license_url: Optional[str] = None
    author: Optional[str] = None
    author_email: Optional[str] = None
    maintainer: Optional[str] = None
    maintainer_email: Optional[str] = None
    metadata_created: Optional[str] = None
    metadata_modified: Optional[str] = None

    # Converters

    def to_dp(self):
        package = Package()

        # Name
        if self.name:
            package.name = self.name

        # Title
        if self.title:
            package.title = self.title

        # Description
        if self.notes:
            package.description = self.notes

        # Version
        if self.version:
            package.version = self.version

        # Created
        if self.metadata_created:
            package.created = self.metadata_created

        # License
        if self.license_id:
            license = License(name=self.license_id)
            if self.license_title:
                license.title = self.license_title
            if self.license_url:
                license.url = self.license_url
            package.licenses.append(license)

        # Contributors
        if self.author:
            contributor = Contributor(title=self.author, role="author")
            if self.author_email:
                contributor.email = self.author_email
            package.contributors.append(contributor)
        if self.maintainer:
            contributor = Contributor(title=self.maintainer, role="maintainer")
            if self.maintainer_email:
                contributor.email = self.maintainer_email
            package.contributors.append(contributor)

        # Resources
        for item in self.resources:
            resource = item.to_dp()
            package.resources.append(resource)

        # Keywords
        for tag in self.tags:
            package.keywords.append(tag.name)

        # Custom
        if self.id:
            package.custom["ckan:id"] = self.id

        return package

    @classmethod
    def from_dp(cls, package: Package) -> CkanPackage:
        ckan = CkanPackage()

        # Name
        if package.name:
            ckan.name = package.name

        # Title
        if package.title:
            ckan.title = package.title

        # Description
        if package.description:
            ckan.notes = package.description

        # Version
        if package.version:
            ckan.version = package.version

        # License
        if package.licenses:
            license = package.licenses[0]
            ckan.license_id = license.name
            if license.title:
                ckan.license_title = license.title
            if license.path:
                ckan.license_url = license.path

        # Contributors
        for contributor in package.contributors:
            if contributor.role == "author":
                ckan.author = contributor.title
                ckan.author_email = contributor.email
            elif contributor.role == "maintainer":
                ckan.maintainer = contributor.title
                ckan.maintainer_email = contributor.email

        # Resources
        for resource in package.resources:
            item = CkanResource.from_dp(resource)
            if item:
                ckan.resources.append(item)

        # Keywords
        for keyword in package.keywords:
            tag = CkanTag(name=keyword)
            ckan.tags.append(tag)

        return ckan
