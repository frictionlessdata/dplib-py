from typing import List, Union

from ... import types
from ...errors.metadata import MetadataError
from ..metadata.check import metadata_check


def dialect_check(dialect: Union[str, types.IDict]) -> List[MetadataError]:
    return metadata_check(dialect, profile_name="table-dialect")
