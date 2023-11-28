from __future__ import annotations

from ...model import Model


class CkanOrganization(Model):
    id: str
    name: str
    title: str
    description: str
