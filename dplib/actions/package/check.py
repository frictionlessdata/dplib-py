from typing import List, Union

from ... import types
from ...errors.metadata import MetadataError
from ..metadata.check import metadata_check


def package_check(package: Union[str, types.IDict]) -> List[MetadataError]:
    return metadata_check(package, profile_name="data-package")
