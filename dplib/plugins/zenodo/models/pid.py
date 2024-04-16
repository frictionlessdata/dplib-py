from __future__ import annotations

from typing import Optional

from dplib.system import Model


class ZenodoPid(Model):
    client: Optional[str] = None
    identifier: str
    provider: str
