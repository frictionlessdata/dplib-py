from typing import List, Union

from ... import types
from ...errors.metadata import MetadataError
from ...helpers.data import read_data
from ...helpers.profile import read_profile
from ...models import Profile
from ..metadata.check import metadata_check


def schema_check(schema: Union[str, types.IDict]) -> List[MetadataError]:
    profile = Profile.from_dict(read_profile("table-schema"))
    if isinstance(schema, str):
        schema = read_data(schema)
    errors = metadata_check(profile, object=schema)
    return errors
