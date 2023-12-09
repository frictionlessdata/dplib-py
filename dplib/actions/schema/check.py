from typing import List, Union

from ... import types
from ...errors.metadata import MetadataError
from ..metadata.check import metadata_check


def schema_check(schema: Union[str, types.IDict]) -> List[MetadataError]:
    return metadata_check(schema, profile_name="table-schema")
