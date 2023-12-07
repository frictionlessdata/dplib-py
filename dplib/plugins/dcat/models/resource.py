from __future__ import annotations

from typing import List, Optional

from rdflib import Graph

from dplib.model import Model

from . import loaders
from . import namespaces as ns
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

    def to_graph(self, g: Graph):
        pass

    @classmethod
    def from_graph(cls, g: Graph, *, id: ISubject) -> DcatResource:
        resource = DcatResource()

        # Name
        name = loaders.string(g, subject=id, predicate=ns.TITLE)
        if name:
            resource.name = name

        # Description
        description = loaders.string(g, subject=id, predicate=ns.DESCRIPTION)
        if description:
            resource.description = description

        # Access URL
        access_url = loaders.string(g, subject=id, predicate=ns.ACCESS_URL)
        if access_url:
            resource.access_url = access_url

        # Download URL
        download_url = loaders.string(g, subject=id, predicate=ns.DOWNLOAD_URL)
        if download_url:
            resource.download_url = download_url

        # Issued
        issued = loaders.string(g, subject=id, predicate=ns.ISSUED)
        if issued:
            resource.issued = issued

        # Modified
        modified = loaders.string(g, subject=id, predicate=ns.MODIFIED)
        if modified:
            resource.modified = modified

        # License
        license = loaders.string(g, subject=id, predicate=ns.LICENSE)
        if license:
            resource.license = license

        # Languages
        languages = loaders.strings(g, subject=id, predicate=ns.LANGUAGE)
        if languages:
            resource.languages = languages

        # Documentations
        documentations = loaders.strings(g, subject=id, predicate=ns.DOCUMENTATION)
        if documentations:
            resource.documentations = documentations

        # Conforms to
        conforms_to = loaders.strings(g, subject=id, predicate=ns.COMFORMS_TO)
        if conforms_to:
            resource.conforms_to = conforms_to

        return resource
