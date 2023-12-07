from __future__ import annotations

from typing import List, Optional

from rdflib import BNode, Graph

from dplib.model import Model

from . import dumpers, loaders
from . import namespaces as ns
from .types import ISubject


class DcatResource(Model):
    title: Optional[str] = None
    description: Optional[str] = None
    access_url: Optional[str] = None
    download_url: Optional[str] = None
    issued: Optional[str] = None
    modified: Optional[str] = None
    license: Optional[str] = None
    byte_size: Optional[int] = None
    media_type: Optional[str] = None

    pages: List[str] = []
    languages: List[str] = []
    conforms_to: List[str] = []

    # Converters

    def to_graph(self, g: Graph, *, id: BNode):
        # Title
        if self.title:
            dumpers.node(g, self.title, subject=id, predicate=ns.TITLE)

        # Description
        if self.description:
            dumpers.node(g, self.description, subject=id, predicate=ns.DESCRIPTION)

        # Access URL
        if self.access_url:
            dumpers.node(g, self.access_url, subject=id, predicate=ns.ACCESS_URL)

        # Download URL
        if self.download_url:
            dumpers.node(g, self.download_url, subject=id, predicate=ns.DOWNLOAD_URL)

        # Issued
        if self.issued:
            dumpers.node(g, self.issued, subject=id, predicate=ns.ISSUED)

        # Modified
        if self.modified:
            dumpers.node(g, self.modified, subject=id, predicate=ns.MODIFIED)

        # License
        if self.license:
            dumpers.node(g, self.license, subject=id, predicate=ns.LICENSE)

        # Byte size
        if self.byte_size:
            dumpers.node(g, self.byte_size, subject=id, predicate=ns.BYTE_SIZE)

        # Media type
        if self.media_type:
            dumpers.node(g, self.media_type, subject=id, predicate=ns.MEDIA_TYPE)

        # Pages
        for page in self.pages:
            dumpers.node(g, page, subject=id, predicate=ns.PAGE)

        # Languages
        for language in self.languages:
            dumpers.node(g, language, subject=id, predicate=ns.LANGUAGE)

        # Conforms to
        for conforms_to in self.conforms_to:
            dumpers.node(g, conforms_to, subject=id, predicate=ns.COMFORMS_TO)

        return g

    @classmethod
    def from_graph(cls, g: Graph, *, id: ISubject) -> DcatResource:
        resource = DcatResource()

        # Name
        title = loaders.string(g, subject=id, predicate=ns.TITLE)
        if title:
            resource.title = title

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

        # Byte size
        byte_size = loaders.integer(g, subject=id, predicate=ns.BYTE_SIZE)
        if byte_size:
            resource.byte_size = byte_size

        # Media type
        media_type = loaders.string(g, subject=id, predicate=ns.MEDIA_TYPE)
        if media_type:
            resource.media_type = media_type

        # Pages
        pages = loaders.strings(g, subject=id, predicate=ns.PAGE)
        if pages:
            resource.pages = pages

        # Languages
        languages = loaders.strings(g, subject=id, predicate=ns.LANGUAGE)
        if languages:
            resource.languages = languages

        # Conforms to
        conforms_to = loaders.strings(g, subject=id, predicate=ns.COMFORMS_TO)
        if conforms_to:
            resource.conforms_to = conforms_to

        return resource
