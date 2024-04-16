from __future__ import annotations

from typing import Dict, Optional

from dplib.system import Model

from .resource import ZenodoResource


class ZenodoFiles(Model):
    entries: Dict[str, ZenodoResource] = {}
    count: Optional[int] = None
    total_bytes: Optional[int] = None
