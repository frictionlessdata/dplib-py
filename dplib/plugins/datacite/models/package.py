from __future__ import annotations

from typing import List, Optional

from dplib.models import Contributor, License, Package
from dplib.system import Model

from .contributor import DataciteContributor, DataciteContributorAffiliation
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
    """Datacite Package model"""

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

    # Converters

    def to_dp(self) -> Package:
        """Convert to Data Package

        Returns:
           Data Package
        """
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
        for type, items in [("creator", self.creators), ("other", self.contributors)]:
            for item in items:
                contributor = Contributor(
                    title=item.name,
                    givenName=item.givenName,
                    familyName=item.familyName,
                )
                if type == "creator":
                    contributor.roles = [type]
                elif item.contributorType:
                    contributor.roles = [item.contributorType]
                for affiliation in item.affiliation:
                    contributor.organization = affiliation.name
                    break
                package.contributors.append(contributor)

        # Licenses
        for rights in self.rightsList:
            if rights.rightsIdentifier or rights.rightsUri:
                license = License(name=rights.rightsIdentifier, path=rights.rightsUri)
                if rights.rights:
                    license.title = rights.rights
                package.licenses.append(license)

        return package

    @classmethod
    def from_dp(cls, package: Package) -> DatacitePackage:
        """Create a Datacite Package from Data Package

        Parameters:
            package: Data Package

        Returns:
            Datacite Package
        """
        datacite = DatacitePackage()

        # Id
        if package.id:
            if package.id.startswith("https://doi.org/"):
                doi = package.id.replace("https://doi.org/", "")
                datacite.identifiers.append(
                    DataciteIdentifier(identifierType="DOI", identifier=doi)
                )

        # Version
        if package.version:
            datacite.version = package.version

        # Title
        if package.title:
            datacite.titles.append(DataciteTitle(title=package.title))

        # Description
        if package.description:
            datacite.descriptions.append(
                DataciteDescription(
                    descriptionType="Abstract",
                    description=package.description,
                )
            )

        # Homepage
        if package.homepage:
            datacite.identifiers.append(
                DataciteIdentifier(identifierType="URL", identifier=package.homepage)
            )

        # Keywords
        for keyword in package.keywords:
            datacite.subjects.append(DataciteSubject(subject=keyword))

        # Contributors
        for contributor in package.contributors:
            item = DataciteContributor(
                name=contributor.title,
                givenName=contributor.givenName,
                familyName=contributor.familyName,
            )
            if contributor.organization:
                org = DataciteContributorAffiliation(name=contributor.organization)
                item.affiliation.append(org)
            target = datacite.contributors
            if contributor.roles:
                item.contributorType = contributor.roles[0]
                if set(contributor.roles).intersection(["author", "creator"]):
                    target = datacite.creators
            target.append(item)

        return datacite
