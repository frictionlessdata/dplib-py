from __future__ import annotations

from typing import List, Optional

from rdflib import FOAF, Graph, Namespace

from dplib.model import Model

from . import loaders
from .types import ISubject


class DcatResource(Model):
    name: Optional[str] = None
    description: Optional[str] = None
    access_url: Optional[str] = None
    download_url: Optional[str] = None
    issued: Optional[str] = None
    modified: Optional[str] = None
    license: Optional[str] = None
    spdx_checksum: Optional[str] = None
    spdx_algorithm: Optional[str] = None

    languages: List[str] = []
    documentations: List[str] = []
    conforms_to: List[str] = []

    # Mappers

    @classmethod
    def from_graph(cls, g: Graph, *, id: ISubject) -> DcatResource:
        resource = DcatResource()

        # Name
        name = loaders.string(g, subject=id, predicate=DCT.title)
        if name:
            resource.name = name

        # Description
        description = loaders.string(g, subject=id, predicate=DCT.description)
        if description:
            resource.description = description

        # Access URL
        access_url = loaders.string(g, subject=id, predicate=DCAT.accessURL)
        if access_url:
            resource.access_url = access_url

        # Download URL
        download_url = loaders.string(g, subject=id, predicate=DCAT.downloadURL)
        if download_url:
            resource.download_url = download_url

        # Issued
        issued = loaders.string(g, subject=id, predicate=DCT.issued)
        if issued:
            resource.issued = issued

        # Modified
        modified = loaders.string(g, subject=id, predicate=DCT.modified)
        if modified:
            resource.modified = modified

        # License
        license = loaders.string(g, subject=id, predicate=DCT.license)
        if license:
            resource.license = license

        # Languages
        languages = loaders.strings(g, subject=id, predicate=DCT.language)
        if languages:
            resource.languages = languages

        # Documentations
        documentations = loaders.strings(g, subject=id, predicate=FOAF.page)
        if documentations:
            resource.documentations = documentations

        # Conforms to
        conforms_to = loaders.strings(g, subject=id, predicate=DCT.conformsTo)
        if conforms_to:
            resource.conforms_to = conforms_to

        return resource


DCAT = Namespace("http://www.w3.org/ns/dcat#")
DCT = Namespace("http://purl.org/dc/terms/")
