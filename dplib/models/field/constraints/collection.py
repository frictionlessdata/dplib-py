from __future__ import annotations

from typing import Optional

from .base import BaseConstraints


class CollectionConstraints(BaseConstraints):
    minLength: Optional[int] = None
    maxLength: Optional[int] = None
