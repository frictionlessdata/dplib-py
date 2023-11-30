from __future__ import annotations

from typing import Optional

from ...model import Model


class CkanResource(Model):
    created: str
    description: str
    format: str  # NOTE: uppercased
    hash: str
    id: str
    last_modified: Optional[str] = None
    metadata_modified: Optional[str] = None
    mimetype: str
    name: str
    size: Optional[int] = None
