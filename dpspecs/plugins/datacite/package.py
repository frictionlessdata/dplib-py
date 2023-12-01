from __future__ import annotations

from typing import List, Optional

from ...model import Model
from ...models import Contributor, License, Package
from .contributor import DataciteContributor
from .description import DataciteDescription
from .identifier import DataciteIdentifier
from .rights import DataciteRights
from .subject import DataciteSubject
from .title import DataciteTitle

# References:
# - https://github.com/inveniosoftware/datacite/blob/master/tests/data/datacite-v4.3-full-example.json
# - https://zenodo.org/records/5770714 (export Datacite JSON)
# - https://schema.datacite.org/meta/kernel-4.3/doc/DataCite-MetadataKernel_v4.3.pdf


class DatacitePackage(Model):
    version: Optional[str] = None
    language: Optional[str] = None
    publisher: Optional[str] = None
    publicationYear: Optional[str] = None
    schemaVersion: Optional[str] = None

    creators: List[DataciteContributor] = []
    contributors: List[DataciteContributor] = []
    descriptions: List[DataciteDescription] = []
    identifiers: List[DataciteIdentifier] = []
    rightsList: List[DataciteRights] = []
    subjects: List[DataciteSubject] = []
    titles: List[DataciteTitle] = []

    # Mappers

    def to_dp(self) -> Package:
        package = Package()

        # Id
        for identifier in self.identifiers:
            if identifier.identifierType == "DOI":
                package.id = f"https://doi.org/{identifier.identifier}"
                break

        # Version
        if self.version:
            package.version = self.version

        # Title
        for title in self.titles:
            if not title.titleType:
                package.title = title.title
                break

        # Description
        for description in self.descriptions:
            if description.descriptionType == "Abstract":
                package.description = description.description
                break

        # Homepage
        for identifier in self.identifiers:
            if identifier.identifierType == "URL":
                package.homepage = identifier.identifier
                break

        # Keywords
        for subject in self.subjects:
            package.keywords.append(subject.subject)

        # Contributors
        for item in self.creators + self.contributors:
            contributor = Contributor(title=item.name)
            if item.contributorType:
                contributor.role = item.contributorType
            for affiliation in item.affiliation:
                contributor.organization = affiliation.name
                break
            package.contributors.append(contributor)

        # Licenses
        for rights in self.rightsList:
            if rights.rightsIdentifier or rights.rightsUrl:
                license = License(name=rights.rightsIdentifier, path=rights.rightsUrl)
                if rights.rights:
                    license.title = rights.rights
                package.licenses.append(license)

        return package
