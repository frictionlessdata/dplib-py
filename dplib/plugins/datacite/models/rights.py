from __future__ import annotations

from typing import Optional

from dplib.system import Model


class DataciteRights(Model):
    rights: Optional[str] = None
    rightsUri: Optional[str] = None
    rightsIdentifier: Optional[str] = None
    rightsIdentifierScheme: Optional[str] = None
    lang: Optional[str] = None
