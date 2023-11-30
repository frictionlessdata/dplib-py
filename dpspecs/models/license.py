from typing import Optional

from ..model import Model


class License(Model):
    name: Optional[str] = None
    path: Optional[str] = None
    title: Optional[str] = None
