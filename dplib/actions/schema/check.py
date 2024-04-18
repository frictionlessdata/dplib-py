from __future__ import annotations

from typing import List, Union

from ... import types
from ...errors.metadata import MetadataError
from ...models import Schema
from ..metadata.check import check_metadata


def check_schema(schema: Union[str, types.IDict, Schema]) -> List[MetadataError]:
    """Check the validity of a Table Schema descriptor

    This validates the descriptor against the JSON Schema profiles to ensure
    conformity with Data Package standard and Data Package extensions.

    Parameters:
        schema: The Table Schema descriptor

    Returns:
        A list of errors
    """
    if isinstance(schema, Schema):
        schema = schema.to_dict()
    return check_metadata(schema, type="schema")
