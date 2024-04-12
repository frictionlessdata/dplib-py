from __future__ import annotations

from typing import List, Union

from ... import types
from ...errors.metadata import MetadataError
from ...helpers.data import read_data
from ...helpers.path import infer_basepath
from ...models import Resource
from ..metadata.check import check_metadata


def check_resource(resource: Union[str, types.IData, Resource]) -> List[MetadataError]:
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
        resource = read_data(resource)
    if isinstance(resource, Resource):
        basepath = resource.basepath
        resource = resource.to_dict()

    # Validate (including nested descriptors)
    errors = check_metadata(resource, type="resource")
    for type in ["dialect", "schema"]:
        value = resource.get(type)
        if isinstance(value, str):
            metadata = read_data(value, basepath=basepath)
            errors.extend(check_metadata(metadata, type=type))  # type: ignore

    return errors
