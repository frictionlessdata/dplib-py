from typing import Optional

from ..model import Model


class Source(Model):
    title: str
    path: Optional[str] = None
    email: Optional[str] = None
