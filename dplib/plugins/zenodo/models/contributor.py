from __future__ import annotations

from typing import List, Optional

import pydantic

from dplib.system import Model


class ZenodoContributorAffiliation(Model):
    name: str


class ZenodoContributorRole(Model):
    id: Optional[str] = None


class ZenodoContributorPersonOrOrg(Model):
    family_name: Optional[str] = None
    given_name: Optional[str] = None
    name: Optional[str] = None
    type: Optional[str] = None


class ZenodoContributor(Model):
    affiliations: List[ZenodoContributorAffiliation] = []
    role: ZenodoContributorRole = pydantic.Field(default_factory=ZenodoContributorRole)
    person_or_org: ZenodoContributorPersonOrOrg = pydantic.Field(
        default_factory=ZenodoContributorPersonOrOrg
    )
