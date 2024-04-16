from __future__ import annotations

from dplib.system import Model


class CkanOrganization(Model):
    id: str
    name: str
    title: str
    description: str
