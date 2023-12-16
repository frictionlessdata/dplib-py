from __future__ import annotations

from typing import List, Union

from ... import types
from ...errors.metadata import MetadataError
from ...helpers.data import read_data
from ...helpers.path import infer_basepath
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
        resource = read_data(resource)
    if isinstance(resource, Resource):
        basepath = resource.basepath
        resource = resource.to_dict()

    # Dereference dialect/schema
    for name in ["dialect", "schema"]:
        value = resource.get(name)
        if value and isinstance(value, str):
            resource[name] = read_data(value, basepath=basepath)

    return check_metadata(resource, type="resource")
