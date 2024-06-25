from typing import List, Optional, Union

from ..system import Model


class MissingValueDict(Model):
    value: str
    label: Optional[str] = None


IMissingValues = Union[
    List[str],
    List[MissingValueDict],
]
