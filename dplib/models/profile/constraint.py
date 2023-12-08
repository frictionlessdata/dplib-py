from typing import Optional

from ... import types
from ...model import Model


class Constraint(Model):
    jsonPath: Optional[str] = None
    jsonSchema: types.IDict = {}
