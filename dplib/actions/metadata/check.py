from typing import List, Union

from ... import types
from ...errors.metadata import MetadataError
from ...helpers.data import read_data
from ...helpers.path import is_remote_path
from ...helpers.profile import read_profile, validate_against_jsonschema
from ...models import Profile


def metadata_check(
    metadata: Union[str, types.IDict], *, profile_name: str
) -> List[MetadataError]:
    if isinstance(metadata, str):
        metadata = read_data(metadata)

    # Base profile
    profile = Profile.from_dict(read_profile(profile_name))
    errors = validate_against_jsonschema(metadata, profile.jsonSchema)

    # Custom profile
    custom_profile = metadata.get("profile")
    if custom_profile and is_remote_path(custom_profile):
        custom_profile = Profile.from_dict(custom_profile)
        errors += validate_against_jsonschema(metadata, custom_profile.jsonSchema)

    return errors
