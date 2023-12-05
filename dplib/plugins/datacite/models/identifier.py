from __future__ import annotations

from dplib.model import Model


class DataciteIdentifier(Model):
    identifier: str
    identifierType: str
