from typing import List, Union

from jsonschema.exceptions import ValidationError

from ... import types
from ...helpers.data import read_data
from ...helpers.profile import read_profile
from ...models import Profile
from ..profile.check import profile_check


def schema_check(schema: Union[str, types.IDict]) -> List[ValidationError]:
    profile = Profile.from_dict(read_profile("table-schema"))
    if isinstance(schema, str):
        schema = read_data(schema)
    errors = profile_check(profile, data=schema)
    return errors
