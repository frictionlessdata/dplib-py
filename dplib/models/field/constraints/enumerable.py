from __future__ import annotations

from typing import Any, Optional

from .base import BaseConstraints


class EnumerabeConstraints(BaseConstraints):
    minimum: Optional[Any] = None
    maximum: Optional[Any] = None
    exclusiveMinimum: Optional[Any] = None
    exclusiveMaximum: Optional[Any] = None
