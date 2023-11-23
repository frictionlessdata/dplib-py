from typing import Optional

from ...model import Model


class ZenodoPid(Model):
    client: Optional[str] = None
    identifier: str
    provider: str
