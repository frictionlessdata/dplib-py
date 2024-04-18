from typing import List, Optional

import pydantic

from .. import types
from ..system import Model


class Contributor(Model):
    title: Optional[str] = None
    givenName: Optional[str] = None
    familyName: Optional[str] = None
    path: Optional[str] = None
    email: Optional[str] = None
    roles: List[str] = []
    organization: Optional[str] = None

    # Compat

    @pydantic.model_validator(mode="before")
    @classmethod
    def compat(cls, data: types.IDict):
        if not isinstance(data, dict):  # type: ignore
            return data

        # contributor.role
        if not data.get("roles"):
            role = data.pop("role", None)
            if role:
                data["roles"] = [role]

        return data
