from typing import Optional

from ..model import Model


class Source(Model):
    title: Optional[str] = None
    path: Optional[str] = None
    email: Optional[str] = None
