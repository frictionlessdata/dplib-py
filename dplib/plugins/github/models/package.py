from __future__ import annotations

from typing import List, Optional

from dplib.models import License, Package
from dplib.system import Model

from .license import GithubLicense
from .owner import GithubOwner
from .resource import GithubResource

# References:
# - https://docs.github.com/en/free-pro-team@latest/rest/repos/repos?apiVersion=2022-11-28#get-a-repository


class GithubPackage(Model):
    """Github Package model"""

    resources: List[GithubResource] = []

    license: Optional[GithubLicense] = None
    owner: Optional[GithubOwner] = None

    private: bool = False
    name: Optional[str] = None
    full_name: Optional[str] = None
    html_url: Optional[str] = None
    description: Optional[str] = None
    pushed_at: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    topics: List[str] = []

    # Converters

    def to_dp(self) -> Package:
        """Convert to Data Package

        Returns:
           Data Package
        """
        package = Package()

        # Title
        if self.name:
            package.title = self.name

        # Name
        if self.full_name:
            package.name = self.full_name

        # Description
        if self.description:
            package.description = self.description

        # Homepage
        if self.html_url:
            package.homepage = self.html_url

        # Created
        if self.created_at:
            package.created = self.created_at

        # License
        if self.license:
            license = License()
            if self.license.spdx_id:
                license.name = self.license.spdx_id
            if self.license.name:
                license.title = self.license.name
            if self.license.html_url:
                license.path = self.license.html_url
            package.licenses.append(license)

        # Keywords
        for topic in self.topics:
            package.keywords.append(topic)

        # Resources
        for item in self.resources:
            resource = item.to_dp()
            package.resources.append(resource)

        return package

    @classmethod
    def from_dp(cls, package: Package) -> GithubPackage:
        """Create a Github Package from Data Package

        Parameters:
            package: Data Package

        Returns:
            Github Package
        """
        github = GithubPackage()

        # Title
        if package.title:
            github.name = package.title

        # Description
        if package.description:
            github.description = package.description

        # Licenses
        if package.licenses:
            license = package.licenses[0]
            github.license = GithubLicense()
            if license.name:
                github.license.spdx_id = license.name
            if license.title:
                github.license.name = license.title
            if license.path:
                github.license.html_url = license.path

        # Keywords
        for keyword in package.keywords:
            github.topics.append(keyword)

        # Resources
        for resource in package.resources:
            item = GithubResource.from_dp(resource)
            if item:
                github.resources.append(item)

        return github
