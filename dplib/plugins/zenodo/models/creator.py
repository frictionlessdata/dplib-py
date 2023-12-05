from __future__ import annotations

from typing import List, Optional

import pydantic

from dplib.model import Model


class ZenodoCreatorAffiliation(Model):
    name: str


class ZenodoCreatorPersonOrOrg(Model):
    family_name: Optional[str] = None
    given_name: Optional[str] = None
    name: Optional[str] = None
    type: Optional[str] = None


class ZenodoCreator(Model):
    affiliations: List[ZenodoCreatorAffiliation] = []
    person_or_org: ZenodoCreatorPersonOrOrg = pydantic.Field(
        default_factory=ZenodoCreatorPersonOrOrg
    )
