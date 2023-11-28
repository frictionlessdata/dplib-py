from __future__ import annotations

from typing import List

from ...model import Model
from .organization import CkanOrganization
from .resource import CkanResource
from .tag import CkanTag

# References:
# - https://demo.ckan.org/api/3/action/package_show?id=sample-dataset-1


class CkanPackage(Model):
    resources: List[CkanResource]

    organization: CkanOrganization
    tags: List[CkanTag]

    id: str
    name: str
    title: str
    notes: str
    author: str
    author_email: str
    license_id: str
    license_title: str
    license_url: str
    maintainer: str
    maintainer_email: str
    metadata_created: str
    metadata_modified: str
