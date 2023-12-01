from __future__ import annotations

from typing import List, Optional

from ...model import Model
from .contributor import DataciteContributor
from .description import DataciteDescription
from .identifier import DataciteIdentifier
from .rights import DataciteRights
from .subject import DataciteSubject
from .title import DataciteTitle

# References:
# - https://github.com/inveniosoftware/datacite/blob/master/tests/data/datacite-v4.3-full-example.json
# - https://zenodo.org/records/5770714 (export Datacite JSON)


class DatacitePackage(Model):
    publisher: Optional[str] = None
    version: Optional[str] = None
    language: Optional[str] = None
    publicationYear: Optional[str] = None

    creators: List[DataciteContributor] = []
    descriptions: List[DataciteDescription] = []
    identifiers: List[DataciteIdentifier] = []
    rightsList: List[DataciteRights] = []
    subjects: List[DataciteSubject] = []
    titles: List[DataciteTitle] = []
