from typing import Union

from jsonschema import validate

from ... import types
from ...helpers.data import load_data
from ...helpers.file import read_file
from ...helpers.profile import read_profile
from ...models import Profile


def schema_check(schema: Union[str, types.IDict]):
    profile = Profile.from_dict(read_profile("table-schema"))
    if isinstance(schema, str):
        text = read_file(schema)
        schema = load_data(text)
    print(profile)
