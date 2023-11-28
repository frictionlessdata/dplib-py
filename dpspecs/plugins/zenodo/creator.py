from __future__ import annotations

from typing import List

from ...model import Model


class ZenodoCreatorAffilation(Model):
    name: str


class ZenodoCreatorPersonOrOrg(Model):
    family_name: str
    given_name: str
    name: str
    type: str


class ZenodoCreator(Model):
    affilations: List[ZenodoCreatorAffilation]
    person_or_org: ZenodoCreatorPersonOrOrg
