from typing import Any, List, Optional

from ...model import Model


class Constraints(Model):
    required: Optional[bool] = None
    unique: Optional[bool] = None
    enum: Optional[List[Any]] = None
    minimum: Optional[str] = None
    maximum: Optional[str] = None
    minLength: Optional[int] = None
    maxLength: Optional[int] = None
    pattern: Optional[str] = None
