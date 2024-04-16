from __future__ import annotations

from typing import List, Optional

from dplib.system import Model


class DataciteContributorAffiliation(Model):
    name: Optional[str] = None
    affiliationIdentifier: Optional[str] = None
    affiliationIdentifierScheme: Optional[str] = None


class DataciteContributor(Model):
    name: Optional[str] = None
    nameType: Optional[str] = None
    givenName: Optional[str] = None
    familyName: Optional[str] = None
    contributorType: Optional[str] = None
    affiliation: List[DataciteContributorAffiliation] = []
