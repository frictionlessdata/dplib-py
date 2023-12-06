from __future__ import annotations

from typing import List, Optional

from dplib.model import Model

# References:
# - https://www.w3.org/TR/vocab-dcat-2/
# - https://joinup.ec.europa.eu/asset/dcat_application_profile


class DcatPackage(Model):
    identifier: str
    type: str
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
