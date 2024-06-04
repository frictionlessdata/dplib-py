from __future__ import annotations

from typing import List, Optional

from dplib.helpers.datetime import add_timezone_infromation
from dplib.models import Contributor, License, Package
from dplib.system import Model

from .organization import CkanOrganization
from .resource import CkanResource
from .tag import CkanTag

# References:
# - https://demo.ckan.org/api/3/action/package_show?id=sample-dataset-1


class CkanPackage(Model):
    """CKAN Package model"""

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

    def to_dp(self) -> Package:
        """Convert to Data Package

        Returns:
           Data Package
        """
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
            package.created = add_timezone_infromation(self.metadata_created)

        # License
        if self.license_id:
            license = License(name=self.license_id)
            if self.license_title:
                license.title = self.license_title
            if self.license_url:
                license.path = self.license_url
            package.licenses.append(license)

        # Contributors
        if self.author:
            contributor = Contributor(title=self.author, roles=["author"])
            if self.author_email:
                contributor.email = self.author_email
            package.contributors.append(contributor)
        if self.maintainer:
            contributor = Contributor(title=self.maintainer, roles=["maintainer"])
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
        """Create a CKAN Package from Data Package

        Parameters:
            package: Data Package

        Returns:
            CKAN Package
        """
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
            if contributor.roles:
                if "author" in contributor.roles:
                    ckan.author = contributor.title
                    ckan.author_email = contributor.email
                elif "maintainer" in contributor.roles:
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
