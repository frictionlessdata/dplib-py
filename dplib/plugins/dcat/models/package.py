from __future__ import annotations

from typing import Any, List, Optional

from rdflib import BNode, Graph, URIRef

from dplib.error import Error
from dplib.models import Package, Source
from dplib.system import Model

from . import dumpers, loaders
from . import namespaces as ns
from .resource import DcatResource

# References:
# - https://www.w3.org/TR/vocab-dcat-2/
# - https://joinup.ec.europa.eu/asset/dcat_application_profile
# - https://github.com/ckan/ckanext-dcat/blob/master/ckanext/dcat/profiles.py


class DcatPackage(Model):
    """DCAT Package model"""

    identifier: Optional[str] = None
    distributions: List[DcatResource] = []

    accural_periodicity: Optional[str] = None
    alternate_identifiers: List[str] = []
    comforms_to: List[str] = []
    description: Optional[str] = None
    has_versions: List[str] = []
    homepage: Optional[str] = None
    issued: Optional[str] = None
    is_version_of: List[str] = []
    keywords: List[str] = []
    landing_page: Optional[str] = None
    languages: List[str] = []
    modified: Optional[str] = None
    pages: List[str] = []
    provenance: Optional[str] = None
    related_resources: List[str] = []
    samples: List[str] = []
    sources: List[str] = []
    themes: List[str] = []
    title: Optional[str] = None
    version: Optional[str] = None

    # Converters

    def to_text(self, *, format: str):
        g = self.to_graph()
        return g.serialize(format=format)

    @classmethod
    def from_text(cls, text: str, *, format: str, **kwargs: Any):
        g = Graph()
        g.parse(data=text, format=format)
        return cls.from_graph(g)

    def to_graph(self):
        g = Graph()
        for prefix, namespace in ns.BINDINGS.items():
            g.bind(prefix, namespace)

        # Identifier
        if not self.identifier:
            raise Error(f"Cannot dump DCAT package without identifier: {self}")
        id = dumpers.id(g, self.identifier, predicate=ns.TYPE, object=ns.DATASET)

        # Accural periodicity
        if self.accural_periodicity:
            dumpers.node(
                g, self.accural_periodicity, subject=id, predicate=ns.ACCURAL_PERIODICITY
            )

        # Alternate identifiers
        for identifier in self.alternate_identifiers:
            dumpers.node(g, identifier, subject=id, predicate=ns.ALTERNATE_IDENTIFIER)

        # Conforms to
        for conforms_to in self.comforms_to:
            dumpers.node(g, conforms_to, subject=id, predicate=ns.COMFORMS_TO)

        # Description
        if self.description:
            dumpers.node(g, self.description, subject=id, predicate=ns.DESCRIPTION)

        # Has versions
        for has_version in self.has_versions:
            dumpers.node(g, has_version, subject=id, predicate=ns.HAS_VERSION)

        # Homepage
        if self.homepage:
            dumpers.node(g, self.homepage, subject=id, predicate=ns.HOMEPAGE)

        # Issued
        if self.issued:
            dumpers.node(g, self.issued, subject=id, predicate=ns.ISSUED)

        # Is version of
        for is_version_of in self.is_version_of:
            dumpers.node(g, is_version_of, subject=id, predicate=ns.IS_VERSION_OF)

        # Keywords
        for keyword in self.keywords:
            dumpers.node(g, keyword, subject=id, predicate=ns.KEYWORD)

        # Landing page
        if self.landing_page:
            dumpers.node(g, self.landing_page, subject=id, predicate=ns.LANDING_PAGE)

        # Languages
        for language in self.languages:
            dumpers.node(g, language, subject=id, predicate=ns.LANGUAGE)

        # Modified
        if self.modified:
            dumpers.node(g, self.modified, subject=id, predicate=ns.MODIFIED)

        # Pages
        for page in self.pages:
            dumpers.node(g, page, subject=id, predicate=ns.PAGE)

        # Provenance
        if self.provenance:
            dumpers.node(g, self.provenance, subject=id, predicate=ns.PROVENANCE)

        # Related resources
        for related_resource in self.related_resources:
            dumpers.node(g, related_resource, subject=id, predicate=ns.RELATED_RESOURCE)

        # Samples
        for sample in self.samples:
            dumpers.node(g, sample, subject=id, predicate=ns.SAMPLE)

        # Sources
        for source in self.sources:
            dumpers.node(g, source, subject=id, predicate=ns.SOURCE)

        # Themes
        for theme in self.themes:
            dumpers.node(g, theme, subject=id, predicate=ns.THEME)

        # Title
        if self.title:
            dumpers.node(g, self.title, subject=id, predicate=ns.TITLE)

        # Version
        if self.version:
            dumpers.node(g, self.version, subject=id, predicate=ns.VERSION)

        # Distributions
        for distribution in self.distributions:
            distribution_id = BNode()
            g.add((id, ns.DISTRIBUTION, distribution_id))
            g.add((distribution_id, ns.TYPE, ns.DISTRIBUTION))
            distribution.to_graph(g, id=distribution_id)

        return g

    @classmethod
    def from_graph(cls, g: Graph):
        package = DcatPackage()

        # Identifier
        id = loaders.id(g, predicate=ns.TYPE, object=ns.DATASET)
        if not id:
            raise Error(f"Cannot load DCAT package without identifier: {g}")
        package.identifier = str(id)

        # Accural periodicity
        periodicity = loaders.string(g, subject=id, predicate=ns.ACCURAL_PERIODICITY)
        if periodicity:
            package.accural_periodicity = periodicity

        # Alternate identifiers
        identifiers = loaders.strings(g, subject=id, predicate=ns.ALTERNATE_IDENTIFIER)
        if identifiers:
            package.alternate_identifiers = identifiers

        # Conforms to
        conforms_to = loaders.strings(g, subject=id, predicate=ns.COMFORMS_TO)
        if conforms_to:
            package.comforms_to = conforms_to

        # Description
        description = loaders.string(g, subject=id, predicate=ns.DESCRIPTION)
        if description:
            package.description = description

        # Has versions
        has_versions = loaders.strings(g, subject=id, predicate=ns.HAS_VERSION)
        if has_versions:
            package.has_versions = has_versions

        # Homepage
        homepage = loaders.string(g, subject=id, predicate=ns.HOMEPAGE)
        if homepage:
            package.homepage = homepage

        # Issued
        issued = loaders.string(g, subject=id, predicate=ns.ISSUED)
        if issued:
            package.issued = issued

        # Is version of
        is_version_of = loaders.strings(g, subject=id, predicate=ns.IS_VERSION_OF)
        if is_version_of:
            package.is_version_of = is_version_of

        # Keywords
        keywords = loaders.strings(g, subject=id, predicate=ns.KEYWORD)
        if keywords:
            package.keywords = keywords

        # Landing page
        landing_page = loaders.string(g, subject=id, predicate=ns.LANDING_PAGE)
        if landing_page:
            package.landing_page = landing_page

        # Languages
        languages = loaders.strings(g, subject=id, predicate=ns.LANGUAGE)
        if languages:
            package.languages = languages

        # Modified
        modified = loaders.string(g, subject=id, predicate=ns.MODIFIED)
        if modified:
            package.modified = modified

        # Pages
        pages = loaders.strings(g, subject=id, predicate=ns.PAGE)
        if pages:
            package.pages = pages

        # Provenance
        provenance = loaders.string(g, subject=id, predicate=ns.PROVENANCE)
        if provenance:
            package.provenance = provenance

        # Related resources
        related_resources = loaders.strings(g, subject=id, predicate=ns.RELATED_RESOURCE)
        if related_resources:
            package.related_resources = related_resources

        # Samples
        samples = loaders.strings(g, subject=id, predicate=ns.SAMPLE)
        if samples:
            package.samples = samples

        # Sources
        sources = loaders.strings(g, subject=id, predicate=ns.SOURCE)
        if sources:
            package.sources = sources

        # Themes
        themes = loaders.strings(g, subject=id, predicate=ns.THEME)
        if themes:
            package.themes = themes

        # Title
        title = loaders.string(g, subject=id, predicate=ns.TITLE)
        if title:
            package.title = title

        # Version
        version = loaders.string(g, subject=id, predicate=ns.VERSION)
        if version:
            package.version = version

        # Distributions
        distributions = g.objects(subject=id, predicate=ns.DISTRIBUTION)
        for distribution in distributions:
            if isinstance(distribution, (URIRef, BNode)):
                resource = DcatResource.from_graph(g, id=distribution)
                package.distributions.append(resource)

        return package

    def to_dp(self) -> Package:
        """Convert to Data Package

        Returns:
           Data Package
        """
        package = Package()

        # Id
        if self.identifier:
            package.id = self.identifier

        # Title
        if self.title:
            package.title = self.title

        # Description
        if self.description:
            package.description = self.description

        # Version
        if self.version:
            package.version = self.version

        # Homepage
        if self.homepage:
            package.homepage = self.homepage

        # Created
        if self.issued:
            if "T" in self.issued:
                package.created = self.issued

        # Keywords
        for keyword in self.keywords:
            package.keywords.append(keyword)

        # Sources
        for source in self.sources:
            source = Source(title=source)
            package.sources.append(source)

        # Resources
        for distribution in self.distributions:
            resource = distribution.to_dp()
            if resource:
                package.resources.append(resource)

        return package

    @classmethod
    def from_dp(cls, package: Package) -> DcatPackage:
        """Create a DCAT Package from Data Package

        Parameters:
            package: Data Package

        Returns:
            DCAT Package
        """
        dcat = DcatPackage()

        # Identifier
        if package.id:
            dcat.identifier = package.id

        # Title
        if package.title:
            dcat.title = package.title

        # Description
        if package.description:
            dcat.description = package.description

        # Version
        if package.version:
            dcat.version = package.version

        # Homepage
        if package.homepage:
            dcat.homepage = package.homepage

        # Issued
        if package.created:
            dcat.issued = package.created

        # Keywords
        for keyword in package.keywords:
            dcat.keywords.append(keyword)

        # Sources
        for source in package.sources:
            source = source.path or source.title
            if source:
                dcat.sources.append(source)

        # Resources
        for resource in package.resources:
            distribution = DcatResource.from_dp(resource)
            if distribution:
                dcat.distributions.append(distribution)

        return dcat
