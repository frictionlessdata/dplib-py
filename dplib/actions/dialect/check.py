from typing import List, Union

from ... import types
from ...errors.metadata import MetadataError
from ..metadata.check import check_metadata


def check_dialect(dialect: Union[str, types.IDict]) -> List[MetadataError]:
    return check_metadata(dialect, type="dialect")
