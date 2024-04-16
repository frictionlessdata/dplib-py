from __future__ import annotations

from typing import List, Optional

from rdflib import BNode, Graph

from dplib.helpers.resource import slugify_name
from dplib.models import License, Resource
from dplib.system import Model

from . import dumpers, loaders
from . import namespaces as ns
from .types import ISubject


class DcatResource(Model):
    """DCAT Resource model"""

    access_url: Optional[str] = None
    byte_size: Optional[int] = None
    conforms_to: List[str] = []
    description: Optional[str] = None
    download_url: Optional[str] = None
    issued: Optional[str] = None
    languages: List[str] = []
    license: Optional[str] = None
    media_type: Optional[str] = None
    modified: Optional[str] = None
    pages: List[str] = []
    title: Optional[str] = None

    # Converters

    def to_graph(self, g: Graph, *, id: BNode):
        # Access URL
        if self.access_url:
            dumpers.node(g, self.access_url, subject=id, predicate=ns.ACCESS_URL)

        # Byte size
        if self.byte_size:
            dumpers.node(g, self.byte_size, subject=id, predicate=ns.BYTE_SIZE)

        # Conforms to
        for conforms_to in self.conforms_to:
            dumpers.node(g, conforms_to, subject=id, predicate=ns.COMFORMS_TO)

        # Description
        if self.description:
            dumpers.node(g, self.description, subject=id, predicate=ns.DESCRIPTION)

        # Download URL
        if self.download_url:
            dumpers.node(g, self.download_url, subject=id, predicate=ns.DOWNLOAD_URL)

        # Issued
        if self.issued:
            dumpers.node(g, self.issued, subject=id, predicate=ns.ISSUED)

        # Languages
        for language in self.languages:
            dumpers.node(g, language, subject=id, predicate=ns.LANGUAGE)

        # License
        if self.license:
            dumpers.node(g, self.license, subject=id, predicate=ns.LICENSE)

        # Media type
        if self.media_type:
            dumpers.node(g, self.media_type, subject=id, predicate=ns.MEDIA_TYPE)

        # Modified
        if self.modified:
            dumpers.node(g, self.modified, subject=id, predicate=ns.MODIFIED)

        # Pages
        for page in self.pages:
            dumpers.node(g, page, subject=id, predicate=ns.PAGE)

        # Title
        if self.title:
            dumpers.node(g, self.title, subject=id, predicate=ns.TITLE)

        return g

    @classmethod
    def from_graph(cls, g: Graph, *, id: ISubject) -> DcatResource:
        resource = DcatResource()

        # Access URL
        access_url = loaders.string(g, subject=id, predicate=ns.ACCESS_URL)
        if access_url:
            resource.access_url = access_url

        # Byte size
        byte_size = loaders.integer(g, subject=id, predicate=ns.BYTE_SIZE)
        if byte_size:
            resource.byte_size = byte_size

        # Conforms to
        conforms_to = loaders.strings(g, subject=id, predicate=ns.COMFORMS_TO)
        if conforms_to:
            resource.conforms_to = conforms_to

        # Description
        description = loaders.string(g, subject=id, predicate=ns.DESCRIPTION)
        if description:
            resource.description = description

        # Download URL
        download_url = loaders.string(g, subject=id, predicate=ns.DOWNLOAD_URL)
        if download_url:
            resource.download_url = download_url

        # Issued
        issued = loaders.string(g, subject=id, predicate=ns.ISSUED)
        if issued:
            resource.issued = issued

        # Languages
        languages = loaders.strings(g, subject=id, predicate=ns.LANGUAGE)
        if languages:
            resource.languages = languages

        # License
        license = loaders.string(g, subject=id, predicate=ns.LICENSE)
        if license:
            resource.license = license

        # Media type
        media_type = loaders.string(g, subject=id, predicate=ns.MEDIA_TYPE)
        if media_type:
            resource.media_type = media_type

        # Modified
        modified = loaders.string(g, subject=id, predicate=ns.MODIFIED)
        if modified:
            resource.modified = modified

        # Pages
        pages = loaders.strings(g, subject=id, predicate=ns.PAGE)
        if pages:
            resource.pages = pages

        # Title
        title = loaders.string(g, subject=id, predicate=ns.TITLE)
        if title:
            resource.title = title

        return resource

    def to_dp(self) -> Optional[Resource]:
        """Convert to Data Package resource

        Returns:
           Data Resource
        """
        if not self.download_url:
            return
        resource = Resource(path=self.download_url, name=slugify_name(self.download_url))

        # Title
        if self.title:
            resource.title = self.title

        # Description
        if self.description:
            resource.description = self.description

        # Media type
        if self.media_type:
            resource.mediatype = self.media_type

        # Bytes
        if self.byte_size:
            resource.bytes = self.byte_size

        # Licenses
        if self.license:
            license = License(path=self.license)
            resource.licenses.append(license)

        return resource

    @classmethod
    def from_dp(cls, resource: Resource) -> Optional[DcatResource]:
        """Create DCAT Resource from Data Resource

        Parameters:
            resource: Data Resource

        Returns:
            DCAT Resource
        """
        dcat = DcatResource()
        if not resource.path or not isinstance(resource.path, str):
            return

        # Download URL
        # TODO: improve logic -- use basepath and allow only urls
        if resource.path:
            dcat.download_url = resource.path

        # Title
        if resource.title:
            dcat.title = resource.title

        # Description
        if resource.description:
            dcat.description = resource.description

        # Media type
        if resource.mediatype:
            dcat.media_type = resource.mediatype

        # Bytes
        if resource.bytes:
            dcat.byte_size = resource.bytes

        # Licenses
        if resource.licenses:
            license = resource.licenses[0]
            if license.path:
                dcat.license = license.path

        return dcat
