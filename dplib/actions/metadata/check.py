from __future__ import annotations

from typing import List, Union

from ... import settings, types
from ...errors.metadata import MetadataError
from ...helpers.data import read_data
from ...helpers.profile import check_profile


def check_metadata(
    metadata: Union[str, types.IData], *, type: types.IMetadataType
) -> List[MetadataError]:
    if isinstance(metadata, str):
        metadata = read_data(metadata)

    # Get default profile
    if type == "dialect":
        default_profile = settings.PROFILE_DEFAULT_DIALECT
    elif type == "package":
        default_profile = settings.PROFILE_DEFAULT_PACKAGE
    elif type == "resource":
        default_profile = settings.PROFILE_DEFAULT_RESOURCE
    elif type == "schema":
        default_profile = settings.PROFILE_DEFAULT_SCHEMA
    else:
        raise ValueError(f"Invalid metadata type: {type}")

    # Validate metadata
    profile = metadata.get("$schema", default_profile)
    errors = check_profile(metadata=metadata, profile=profile)

    return errors
