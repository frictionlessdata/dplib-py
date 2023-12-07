from __future__ import annotations

from typing import List, Optional

from rdflib import BNode, Graph, URIRef

from dplib.error import Error
from dplib.model import Model

from . import dumpers, loaders
from . import namespaces as ns
from .resource import DcatResource

# References:
# - https://www.w3.org/TR/vocab-dcat-2/
# - https://joinup.ec.europa.eu/asset/dcat_application_profile
# - https://github.com/ckan/ckanext-dcat/blob/master/ckanext/dcat/profiles.py


class DcatPackage(Model):
    identifier: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    version: Optional[str] = None
    landing_page: Optional[str] = None
    issued: Optional[str] = None
    modified: Optional[str] = None
    accural_periodicity: Optional[str] = None
    provenance: Optional[str] = None

    keywords: List[str] = []
    languages: List[str] = []
    sources: List[str] = []
    samples: List[str] = []
    themes: List[str] = []
    pages: List[str] = []
    comforms_to: List[str] = []
    has_versions: List[str] = []
    is_version_of: List[str] = []
    related_resources: List[str] = []
    alternate_identifiers: List[str] = []

    distributions: List[DcatResource] = []

    # Mappers

    def to_text(self, *, format: str):
        g = self.to_graph()
        return g.serialize(format=format)

    @classmethod
    def from_text(cls, text: str, *, format: str):
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

        # Title
        if self.title:
            dumpers.node(g, self.title, subject=id, predicate=ns.TITLE)

        # Description
        if self.description:
            dumpers.node(g, self.description, subject=id, predicate=ns.DESCRIPTION)

        # Version
        if self.version:
            dumpers.node(g, self.version, subject=id, predicate=ns.VERSION)

        # Landing page
        if self.landing_page:
            dumpers.node(g, self.landing_page, subject=id, predicate=ns.LANDING_PAGE)

        # Issued
        if self.issued:
            dumpers.node(g, self.issued, subject=id, predicate=ns.ISSUED)

        # Modified
        if self.modified:
            dumpers.node(g, self.modified, subject=id, predicate=ns.MODIFIED)

        # Accural periodicity
        if self.accural_periodicity:
            dumpers.node(
                g, self.accural_periodicity, subject=id, predicate=ns.ACCURAL_PERIODICITY
            )

        # Provenance
        if self.provenance:
            dumpers.node(g, self.provenance, subject=id, predicate=ns.PROVENANCE)

        # Keywords
        for keyword in self.keywords:
            dumpers.node(g, keyword, subject=id, predicate=ns.KEYWORD)

        # Languages
        for language in self.languages:
            dumpers.node(g, language, subject=id, predicate=ns.LANGUAGE)

        # Sources
        for source in self.sources:
            dumpers.node(g, source, subject=id, predicate=ns.SOURCE)

        # Samples
        for sample in self.samples:
            dumpers.node(g, sample, subject=id, predicate=ns.SAMPLE)

        # Themes
        for theme in self.themes:
            dumpers.node(g, theme, subject=id, predicate=ns.THEME)

        # Pages
        for page in self.pages:
            dumpers.node(g, page, subject=id, predicate=ns.PAGE)

        # Conforms to
        for conforms_to in self.comforms_to:
            dumpers.node(g, conforms_to, subject=id, predicate=ns.COMFORMS_TO)

        # Has versions
        for has_version in self.has_versions:
            dumpers.node(g, has_version, subject=id, predicate=ns.HAS_VERSION)

        # Is version of
        for is_version_of in self.is_version_of:
            dumpers.node(g, is_version_of, subject=id, predicate=ns.IS_VERSION_OF)

        # Related resources
        for related_resource in self.related_resources:
            dumpers.node(g, related_resource, subject=id, predicate=ns.RELATED_RESOURCE)

        # Alternate identifiers
        for identifier in self.alternate_identifiers:
            dumpers.node(g, identifier, subject=id, predicate=ns.ALTERNATE_IDENTIFIER)

        return g

    @classmethod
    def from_graph(cls, g: Graph):
        package = DcatPackage()

        # Identifier
        id = loaders.id(g, predicate=ns.TYPE, object=ns.DATASET)
        if not id:
            raise Error(f"Cannot load DCAT package without identifier: {g}")
        package.identifier = str(id)

        # Title
        title = loaders.string(g, subject=id, predicate=ns.TITLE)
        if title:
            package.title = title

        # Description
        description = loaders.string(g, subject=id, predicate=ns.DESCRIPTION)
        if description:
            package.description = description

        # Version
        version = loaders.string(g, subject=id, predicate=ns.VERSION)
        if version:
            package.version = version

        # Landing page
        landing_page = loaders.string(g, subject=id, predicate=ns.LANDING_PAGE)
        if landing_page:
            package.landing_page = landing_page

        # Issued
        issued = loaders.string(g, subject=id, predicate=ns.ISSUED)
        if issued:
            package.issued = issued

        # Modified
        modified = loaders.string(g, subject=id, predicate=ns.MODIFIED)
        if modified:
            package.modified = modified

        # Accural periodicity
        periodicity = loaders.string(g, subject=id, predicate=ns.ACCURAL_PERIODICITY)
        if periodicity:
            package.accural_periodicity = periodicity

        # Provenance
        provenance = loaders.string(g, subject=id, predicate=ns.PROVENANCE)
        if provenance:
            package.provenance = provenance

        # Keywords
        keywords = loaders.strings(g, subject=id, predicate=ns.KEYWORD)
        if keywords:
            package.keywords = keywords

        # Languages
        languages = loaders.strings(g, subject=id, predicate=ns.LANGUAGE)
        if languages:
            package.languages = languages

        # Sources
        sources = loaders.strings(g, subject=id, predicate=ns.SOURCE)
        if sources:
            package.sources = sources

        # Samples
        samples = loaders.strings(g, subject=id, predicate=ns.SAMPLE)
        if samples:
            package.samples = samples

        # Themes
        themes = loaders.strings(g, subject=id, predicate=ns.THEME)
        if themes:
            package.themes = themes

        # Pages
        pages = loaders.strings(g, subject=id, predicate=ns.PAGE)
        if pages:
            package.pages = pages

        # Conforms to
        conforms_to = loaders.strings(g, subject=id, predicate=ns.COMFORMS_TO)
        if conforms_to:
            package.comforms_to = conforms_to

        # Has versions
        has_versions = loaders.strings(g, subject=id, predicate=ns.HAS_VERSION)
        if has_versions:
            package.has_versions = has_versions

        # Is version of
        is_version_of = loaders.strings(g, subject=id, predicate=ns.IS_VERSION_OF)
        if is_version_of:
            package.is_version_of = is_version_of

        # Related resources
        related_resources = loaders.strings(g, subject=id, predicate=ns.RELATED_RESOURCE)
        if related_resources:
            package.related_resources = related_resources

        # Alternate identifiers
        identifiers = loaders.strings(g, subject=id, predicate=ns.ALTERNATE_IDENTIFIER)
        if identifiers:
            package.alternate_identifiers = identifiers

        # Distributions
        distributions = g.objects(subject=id, predicate=ns.DISTRIBUTION)
        for distribution in distributions:
            if isinstance(distribution, (URIRef, BNode)):
                resource = DcatResource.from_graph(g, id=distribution)
                package.distributions.append(resource)

        return package
