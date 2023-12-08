from typing import Optional

from ... import types
from ...model import Model


class Profile(Model):
    title: Optional[str] = None
    description: Optional[str] = None
    jsonSchema: types.IDict = {}
