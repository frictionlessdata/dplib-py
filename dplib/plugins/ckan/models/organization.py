from __future__ import annotations

from dplib.model import Model


class CkanOrganization(Model):
    id: str
    name: str
    title: str
    description: str
