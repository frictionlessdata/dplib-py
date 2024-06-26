from typing import List, Optional, Union

from ...system import Model


class CategoryDict(Model):
    value: str
    label: Optional[str] = None


ICategories = Union[
    List[str],
    List[CategoryDict],
]
