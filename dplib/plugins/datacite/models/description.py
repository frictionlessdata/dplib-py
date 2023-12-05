from __future__ import annotations

from dplib.model import Model


class DataciteDescription(Model):
    description: str
    descriptionType: str
