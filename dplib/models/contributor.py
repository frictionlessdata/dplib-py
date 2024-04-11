from typing import List, Optional
from pydantic import model_validator

from .. import types
from ..model import Model


class Contributor(Model):
    title: Optional[str] = None
    givenName: Optional[str] = None
    familyName: Optional[str] = None
    path: Optional[str] = None
    email: Optional[str] = None
    roles: Optional[List[str]] = []
    organization: Optional[str] = None

    # Compat

    @model_validator(mode="before")
    @classmethod
    def compat_standard_v1(cls, data: types.IData):
        # contributor.role
        if not data.get("roles"):
            role = data.pop("role", None)
            if role:
                data["roles"] = [role]
        return data
