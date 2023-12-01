from __future__ import annotations

from ...model import Model


class DataciteIdentifier(Model):
    identifier: str
    identifierType: str
