from __future__ import annotations

from typing import List, Union

from ... import types
from ...errors.metadata import MetadataError
from ...helpers.dict import read_dict
from ...helpers.path import assert_safe_path, infer_basepath
from ...models import Resource
from ..metadata.check import check_metadata


def check_resource(resource: Union[str, types.IDict, Resource]) -> List[MetadataError]:
    """Check the validity of a Data Resource descriptor

    This validates the descriptor against the JSON Schema profiles to ensure
    conformity with Data Package standard and Data Package extensions.

    Parameters:
        resource: The Data Resource descriptor

    Returns:
        A list of errors
    """
    basepath = None
    if isinstance(resource, str):
        basepath = infer_basepath(resource)
        resource = read_dict(resource)
    if isinstance(resource, Resource):
        basepath = resource.basepath
        resource = resource.to_dict()

    # Validate (including nested descriptors)
    errors = check_metadata(resource, type="resource")
    for type in ["dialect", "schema"]:
        value = resource.get(type)
        if isinstance(value, str):
            assert_safe_path(value, basepath=basepath)
            metadata = read_dict(value, basepath=basepath)
            errors.extend(check_metadata(metadata, type=type))  # type: ignore

    return errors
