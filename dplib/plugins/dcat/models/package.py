from __future__ import annotations

from typing import List, Optional

from rdflib import Graph
from rdflib.namespace import FOAF, RDF, Namespace

from dplib.model import Model

from . import parsers
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
    themes: List[str] = []
    alternate_identifiers: List[str] = []
    comforms_to: List[str] = []
    documentation: List[str] = []
    related_resources: List[str] = []
    has_versions: List[str] = []
    is_version_of: List[str] = []
    sources: List[str] = []
    samples: List[str] = []

    distributions: List[DcatResource] = []

    # Mappers

    @classmethod
    def from_text(cls, text: str, *, format: str = "xml") -> Optional[DcatPackage]:
        g = Graph()
        g.parse(data=text, format=format)
        package = DcatPackage()

        # Identifier
        id = parsers.id(g, predicate=RDF.type, object=DCAT.Dataset)
        if not id:
            return
        package.identifier = str(id)

        # Title
        title = parsers.string(g, subject=id, predicate=DCT.title)
        if title:
            package.title = title

        # Description
        description = parsers.string(g, subject=id, predicate=DCT.description)
        if description:
            package.description = description

        # Version
        version = parsers.string(g, subject=id, predicate=OWL.versionInfo)
        if version:
            package.version = version

        # Landing page
        landing_page = parsers.string(g, subject=id, predicate=DCAT.landingPage)
        if landing_page:
            package.landing_page = landing_page

        # Issued
        issued = parsers.string(g, subject=id, predicate=DCT.issued)
        if issued:
            package.issued = issued

        # Modified
        modified = parsers.string(g, subject=id, predicate=DCT.modified)
        if modified:
            package.modified = modified

        # Accural periodicity
        periodicity = parsers.string(g, subject=id, predicate=DCT.accrualPeriodicity)
        if periodicity:
            package.accural_periodicity = periodicity

        # Provenance
        provenance = parsers.string(g, subject=id, predicate=DCT.provenance)
        if provenance:
            package.provenance = provenance

        # Keywords
        keywords = parsers.strings(g, subject=id, predicate=DCAT.keyword)
        if keywords:
            package.keywords = keywords

        # Languages
        languages = parsers.strings(g, subject=id, predicate=DCT.language)
        if languages:
            package.languages = languages

        # Themes
        themes = parsers.strings(g, subject=id, predicate=DCAT.theme)
        if themes:
            package.themes = themes

        # Alternate identifiers
        identifiers = parsers.strings(g, subject=id, predicate=ADMS.identifier)
        if identifiers:
            package.alternate_identifiers = identifiers

        # Conforms to
        conforms_to = parsers.strings(g, subject=id, predicate=DCT.conformsTo)
        if conforms_to:
            package.comforms_to = conforms_to

        # Documentation
        documentation = parsers.strings(g, subject=id, predicate=FOAF.page)
        if documentation:
            package.documentation = documentation

        # Related resources
        related_resources = parsers.strings(g, subject=id, predicate=DCT.relation)
        if related_resources:
            package.related_resources = related_resources

        # Has versions
        has_versions = parsers.strings(g, subject=id, predicate=DCT.hasVersion)
        if has_versions:
            package.has_versions = has_versions

        # Is version of
        is_version_of = parsers.strings(g, subject=id, predicate=DCT.isVersionOf)
        if is_version_of:
            package.is_version_of = is_version_of

        # Sources
        sources = parsers.strings(g, subject=id, predicate=DCT.source)
        if sources:
            package.sources = sources

        # Samples
        samples = parsers.strings(g, subject=id, predicate=ADMS.sample)
        if samples:
            package.samples = samples

        return package


ADMS = Namespace("http://www.w3.org/ns/adms#")
DCAT = Namespace("http://www.w3.org/ns/dcat#")
DCT = Namespace("http://purl.org/dc/terms/")
OWL = Namespace("http://www.w3.org/2002/07/owl#")