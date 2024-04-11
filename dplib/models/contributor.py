from typing import List, Optional

from ..model import Model


class Contributor(Model):
    title: Optional[str] = None
    givenName: Optional[str] = None
    familyName: Optional[str] = None
    path: Optional[str] = None
    email: Optional[str] = None
    roles: Optional[List[str]] = None
    organization: Optional[str] = None
