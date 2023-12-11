from typing import List, Union

from ... import types
from ...errors.metadata import MetadataError
from ...helpers.data import read_data
from ...helpers.path import infer_basepath
from ..metadata.check import metadata_check


def resource_check(resource: Union[str, types.IDict]) -> List[MetadataError]:
    basepath = None
    if isinstance(resource, str):
        basepath = infer_basepath(resource)
        resource = read_data(resource)

    # Dereference dialect/schema
    for name in ["dialect", "schema"]:
        value = resource.get(name)
        if value and isinstance(value, str):
            resource[name] = read_data(value, basepath=basepath)

    return metadata_check(resource, profile_name="data-resource")
