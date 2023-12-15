from __future__ import annotations

from typing import List, Union

from ... import types
from ...errors.metadata import MetadataError
from ...helpers.data import read_data
from ...helpers.path import is_remote_path
from ...helpers.profile import check_metadata_against_jsonschema, read_profile
from ...models import Profile


def check_metadata(
    metadata: Union[str, types.IDict], *, type: str
) -> List[MetadataError]:
    if isinstance(metadata, str):
        metadata = read_data(metadata)

    # Base profile
    profile = Profile.from_dict(read_profile(metadata_type=type))
    errors = check_metadata_against_jsonschema(metadata, profile.jsonSchema)

    # Custom profile
    custom_profile = metadata.get("profile")
    if custom_profile and is_remote_path(custom_profile):
        custom_profile = Profile.from_path(custom_profile)
        errors += check_metadata_against_jsonschema(metadata, custom_profile.jsonSchema)

    return errors
