from __future__ import annotations

from typing import List, Union

from ... import types
from ...errors.metadata import MetadataError
from ...models import Dialect
from ..metadata.check import check_metadata


def check_dialect(dialect: Union[str, types.IDict, Dialect]) -> List[MetadataError]:
    if isinstance(dialect, Dialect):
        dialect = dialect.to_dict()
    return check_metadata(dialect, type="dialect")
