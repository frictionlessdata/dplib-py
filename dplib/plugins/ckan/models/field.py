from __future__ import annotations

from dplib.system import Model


class CkanFieldInfo(Model):
    """CKAN FieldInfo model"""

    label: str
    notes: str
    type_override: str


class CkanField(Model):
    """CKAN Field model"""

    id: str
    type: str
    info: CkanFieldInfo
