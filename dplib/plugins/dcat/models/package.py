from __future__ import annotations

from typing import List, Optional

from rdflib import Graph, URIRef
from rdflib.namespace import RDF, Namespace

from dplib.model import Model

from . import parsers

# References:
# - https://www.w3.org/TR/vocab-dcat-2/
# - https://joinup.ec.europa.eu/asset/dcat_application_profile


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
    source: List[str] = []
    sample: List[str] = []

    # Mappers

    @classmethod
    def from_xml(cls, text: str) -> Optional[DcatPackage]:
        g = Graph()
        g.parse(text, format="xml")
        package = DcatPackage()

        # Identifier
        try:
            id = g.value(predicate=RDF.type, object=DCAT.Dataset)
            if not isinstance(id, URIRef):
                return
            package.identifier = str(id)
        except Exception:
            return

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

        return package


DCT = Namespace("http://purl.org/dc/terms/")
DCAT = Namespace("http://www.w3.org/ns/dcat#")
OWL = Namespace("http://www.w3.org/2002/07/owl#")
