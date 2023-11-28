from __future__ import annotations

from typing import List, Optional

from ...model import Model
from .license import GithubLicense
from .organization import GithubOrganization
from .resource import GithubResource

# References:
# - https://docs.github.com/en/free-pro-team@latest/rest/repos/repos?apiVersion=2022-11-28#get-a-repository


class GithubPackage(Model):
    resources: List[GithubResource]

    license: Optional[GithubLicense] = None
    organization: GithubOrganization

    id: int
    name: str
    full_name: str
    html_url: str
    private: bool
    topics: List[str]
    description: Optional[str] = None
    pushed_at: str
    created_at: str
    updated_at: str
