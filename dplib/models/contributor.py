from typing import Optional

from ..model import Model


class Contributor(Model):
    title: Optional[str] = None
    path: Optional[str] = None
    email: Optional[str] = None
    role: Optional[str] = None
    organization: Optional[str] = None
