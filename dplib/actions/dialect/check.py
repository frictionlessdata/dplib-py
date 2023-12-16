from __future__ import annotations

from typing import List, Union

from ... import types
from ...errors.metadata import MetadataError
from ...models import Dialect
from ..metadata.check import check_metadata


def check_dialect(dialect: Union[str, types.IDict, Dialect]) -> List[MetadataError]:
    """Check the validity of a Table Dialect descriptor

    This validates the descriptor against the JSON Schema profiles to ensure
    conformity with Data Package standard and Data Package extensions.

    Parameters:
        dialect: The Table Dialect descriptor

    Returns:
        A list of errors
    """
    if isinstance(dialect, Dialect):
        dialect = dialect.to_dict()
    return check_metadata(dialect, type="dialect")
