from __future__ import annotations

from typing import List, Optional

import pydantic

from ...model import Model


class ZenodoCreatorAffilation(Model):
    name: str


class ZenodoCreatorPersonOrOrg(Model):
    family_name: Optional[str] = None
    given_name: Optional[str] = None
    name: Optional[str] = None
    type: Optional[str] = None


class ZenodoCreator(Model):
    affilations: List[ZenodoCreatorAffilation] = []
    person_or_org: ZenodoCreatorPersonOrOrg = pydantic.Field(
        default_factory=ZenodoCreatorPersonOrOrg
    )
