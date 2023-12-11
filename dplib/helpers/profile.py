import os
from functools import lru_cache
from typing import List

from jsonschema.validators import validator_for  # type: ignore

from .. import types
from ..error import Error
from ..errors.metadata import MetadataError
from .data import load_data
from .file import read_file


@lru_cache
def read_profile(name: str) -> types.IDict:
    format = "json"
    path = os.path.join(os.path.dirname(__file__), "..", "profiles", f"{name}.{format}")
    try:
        text = read_file(path)
    except Exception:
        raise Error(f'Cannot read profile "{name}" at "{path}"')
    data = load_data(text, format=format)
    return data


def validate_against_jsonschema(
    metadata: types.IDict, jsonSchema: types.IDict
) -> List[MetadataError]:
    Validator = validator_for(jsonSchema)  # type: ignore
    validator = Validator(jsonSchema)  # type: ignore
    errors: List[MetadataError] = []
    for validation_error in validator.iter_errors(metadata):  # type: ignore
        errors.append(MetadataError(validation_error))  # type: ignore
    return errors
