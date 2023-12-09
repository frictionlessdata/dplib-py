from typing import List, Union

from ... import types
from ...errors.metadata import MetadataError
from ...helpers.data import read_data
from ...helpers.profile import read_profile
from ...models import Profile
from ..metadata.check import metadata_check


def schema_check(schema: Union[str, types.IDict]) -> List[MetadataError]:
    metadata = schema if isinstance(schema, dict) else read_data(schema)
    profile = Profile.from_dict(read_profile("table-schema"))
    errors = metadata_check(metadata, profile=profile)
    return errors
