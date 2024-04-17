from __future__ import annotations

from typing import Optional

from .collection import CollectionConstraints


class StringConstraints(CollectionConstraints):
    pattern: Optional[str] = None
