from __future__ import annotations

from typing import List, Optional

from ...model import Model
from ...models import Package
from .license import GithubLicense
from .owner import GithubOwner
from .resource import GithubResource

# References:
# - https://docs.github.com/en/free-pro-team@latest/rest/repos/repos?apiVersion=2022-11-28#get-a-repository


class GithubPackage(Model):
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

    # Mappers

    def to_dp(self):
        package = Package()

        # Resources
        for item in self.resources:
            resource = item.to_dp()
            package.resources.append(resource)

        return package

    @classmethod
    def from_dp(cls, package: Package) -> GithubPackage:
        github = GithubPackage()

        # Resources
        for resource in package.resources:
            item = GithubResource.from_dp(resource)
            if item:
                github.resources.append(item)

        return github
