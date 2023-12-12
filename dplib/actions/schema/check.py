from typing import List, Union

from ... import types
from ...errors.metadata import MetadataError
from ..metadata.check import check_metadata


def check_schema(schema: Union[str, types.IDict]) -> List[MetadataError]:
    return check_metadata(schema, type="schema")
