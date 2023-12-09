from typing import List, Union

from ... import types
from ...errors.metadata import MetadataError
from ..metadata.check import metadata_check


def resource_check(resource: Union[str, types.IDict]) -> List[MetadataError]:
    return metadata_check(resource, profile_name="data-resource")
