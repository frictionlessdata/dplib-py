from __future__ import annotations

from typing import Optional

from ...model import Model


class DataciteRights(Model):
    rights: Optional[str] = None
    rightsIdentifier: Optional[str] = None
    rightsIdentifierScheme: Optional[str] = None
    rightsUrl: Optional[str] = None
