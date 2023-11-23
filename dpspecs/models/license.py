from typing import Optional

from ..model import Model


class License(Model):
    name: str
    path: Optional[str] = None
    title: Optional[str] = None
