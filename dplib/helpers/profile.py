from __future__ import annotations

import os
from functools import lru_cache
from typing import List

from jsonschema.validators import validator_for  # type: ignore

from .. import settings, types
from ..error import Error
from ..errors.metadata import MetadataError
from .data import load_data
from .file import read_file

# TODO: implement additional user-side profile caching


def check_profile(*, metadata: types.IData, profile: str) -> List[MetadataError]:
    # Prepare validator
    jsonSchema = read_profile(profile=profile)
    Validator = validator_for(jsonSchema)  # type: ignore
    validator = Validator(jsonSchema)  # type: ignore

    # Validate metadata
    errors: List[MetadataError] = []
    for validation_error in validator.iter_errors(metadata):  # type: ignore
        errors.append(MetadataError(validation_error))  # type: ignore

    return errors


@lru_cache
def read_profile(*, profile: str) -> types.IData:
    parts = parse_profile(profile)

    # Replace with builtin copy
    if parts:
        version, filename = parts
        profile = os.path.join(settings.PROFILE_BASEDIR, version, filename)

    # Read jsonSchema
    try:
        text = read_file(profile)
        data = load_data(text, format="json")
    except Exception:
        raise Error(f'Cannot read profile: "{profile}"')

    return data


def parse_profile(profile: str):
    parts = profile.rsplit("/", 3)

    # Ensure builtin copy exists
    if len(parts) != 3:
        return None
    if parts[0] != settings.PROFILE_BASEURL:
        return None
    if parts[1] not in os.listdir(settings.PROFILE_BASEDIR):
        return None
    if parts[2] not in os.listdir(os.path.join(settings.PROFILE_BASEDIR, parts[1])):
        return None

    return parts[1], parts[2]
