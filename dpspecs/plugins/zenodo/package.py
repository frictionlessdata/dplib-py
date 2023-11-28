from __future__ import annotations

from typing import Dict, List

from ...model import Model
from .files import ZenodoFiles
from .metadata import ZenodoMetadata
from .pid import ZenodoPid

# References:
# - https://zenodo.org/records/6533675


class ZenodoPackage(Model):
    files: ZenodoFiles

    metadata: ZenodoMetadata
    pids: List[ZenodoPid]

    id: str
    created: str
    updated: str
    links: Dict[str, str]
