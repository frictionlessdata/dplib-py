from typing import Union

from ... import types
from ...helpers.profile import read_profile
from ...models import Profile


def schema_check(schema: Union[str, types.IDict]):
    profile = Profile.from_dict(read_profile("table-schema"))
    print(profile)
