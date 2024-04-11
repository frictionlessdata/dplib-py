from __future__ import annotations

from typing import Literal, Union

FieldsMatch = Union[
    Literal["exact"],
    Literal["equal"],
    Literal["subset"],
    Literal["superset"],
    Literal["partial"],
]
