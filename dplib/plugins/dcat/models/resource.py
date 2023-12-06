from __future__ import annotations

from typing import List, Optional

from dplib.model import Model


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
