from __future__ import annotations

from typing import List, Optional

from dplib.model import Model


class DataciteContributorAffiliation(Model):
    name: str
    affiliationIdentifier: Optional[str] = None
    affiliationIdentifierScheme: Optional[str] = None


class DataciteContributor(Model):
    name: str
    nameType: Optional[str] = None
    givenName: Optional[str] = None
    familyName: Optional[str] = None
    contributorType: Optional[str] = None
    affiliation: List[DataciteContributorAffiliation] = []
