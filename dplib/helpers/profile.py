from __future__ import annotations

import os
from functools import lru_cache
from typing import List

from jsonschema.validators import validator_for  # type: ignore

from .. import settings, types
from ..error import Error
from ..errors.metadata import MetadataError
from .dict import load_dict
from .file import read_file
from .path import is_http_or_ftp_protocol_path

# TODO: implement additional user-side profile caching


def check_against_profile(*, metadata: types.IDict, profile: str) -> List[MetadataError]:
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
def read_profile(*, profile: str) -> types.IDict:
    parts = parse_profile(profile)

    # Replace with builtin copy
    if parts:
        version, filename = parts
        profile = os.path.join(settings.PROFILE_BASEDIR, version, filename)

    # Ensure profile is URL
    if not is_http_or_ftp_protocol_path(profile):
        raise Error(f'Profile MUST be a URL: "{profile}"')

    # Read jsonSchema
    try:
        text = read_file(profile)
        data = load_dict(text, format="json")
    except Exception:
        raise Error(f'Profile MUST be resolvable: "{profile}"')

    # Validate jsonSchema
    try:
        Validator = validator_for(data)  # type: ignore
        Validator.check_schema(data)  # type: ignore
    except Exception:
        raise Error(f'Profile MUST resolve to a valid JSON Schema: "{profile}"')

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
