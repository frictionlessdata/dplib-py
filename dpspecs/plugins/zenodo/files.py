from typing import Dict

from ...model import Model
from .resource import ZenodoResource


class ZenodoFiles(Model):
    count: int
    total_bytes: int
    entries: Dict[str, ZenodoResource]
