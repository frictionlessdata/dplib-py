from __future__ import annotations

from typing import Any, List, Optional

from ....system import Model


class BaseConstraints(Model):
    required: Optional[bool] = None
    unique: Optional[bool] = None
    enum: Optional[List[Any]] = None
