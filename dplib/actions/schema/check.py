from __future__ import annotations

from typing import List, Union

from ... import types
from ...errors.metadata import MetadataError
from ...models import Schema
from ..metadata.check import check_metadata


def check_schema(schema: Union[str, types.IDict, Schema]) -> List[MetadataError]:
    if isinstance(schema, Schema):
        schema = schema.to_dict()
    return check_metadata(schema, type="schema")
