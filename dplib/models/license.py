from typing import Optional

from ..system import Model


class License(Model):
    name: Optional[str] = None
    path: Optional[str] = None
    title: Optional[str] = None
