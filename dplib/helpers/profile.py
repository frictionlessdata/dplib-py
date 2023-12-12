from __future__ import annotations

import os
from functools import lru_cache
from typing import List

from jsonschema.validators import validator_for  # type: ignore

from .. import types
from ..error import Error
from ..errors.metadata import MetadataError
from .data import load_data
from .file import read_file


def select_profile(*, metadata_type: types.IMetadataType) -> str:
    if metadata_type == "package":
        return "data-package"
    elif metadata_type == "resource":
        return "data-resource"
    elif metadata_type == "dialect":
        return "table-dialect"
    elif metadata_type == "schema":
        return "table-schema"
    raise Error(f'Invalid metadata type "{metadata_type}"')


@lru_cache
def read_profile(*, metadata_type: types.IMetadataType) -> types.IDict:
    format = "json"
    name = select_profile(metadata_type=metadata_type)
    path = os.path.join(os.path.dirname(__file__), "..", "profiles", f"{name}.{format}")
    try:
        text = read_file(path)
        data = load_data(text, format=format)
    except Exception:
        raise Error(f'Cannot read profile "{name}" at "{path}"')
    return data


def check_metadata_against_jsonschema(
    metadata: types.IDict, jsonSchema: types.IDict
) -> List[MetadataError]:
    Validator = validator_for(jsonSchema)  # type: ignore
    validator = Validator(jsonSchema)  # type: ignore
    errors: List[MetadataError] = []
    for validation_error in validator.iter_errors(metadata):  # type: ignore
        errors.append(MetadataError(validation_error))  # type: ignore
    return errors
