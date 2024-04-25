from __future__ import annotations

from typing import List, Union

from ... import types
from ...errors.metadata import MetadataError
from ...helpers.dict import read_dict
from ...helpers.path import assert_safe_path, infer_basepath
from ...models import Package
from ..metadata.check import check_metadata


def check_package(package: Union[str, types.IDict, Package]) -> List[MetadataError]:
    """Check the validity of a Data Package descriptor

    This validates the descriptor against the JSON Schema profiles to ensure
    conformity with Data Package standard and Data Package extensions.

    Parameters:
        package: The Data Package descriptor

    Returns:
        A list of errors
    """
    basepath = None
    if isinstance(package, str):
        basepath = infer_basepath(package)
        package = read_dict(package)
    if isinstance(package, Package):
        basepath = package.basepath
        package = package.to_dict()

    # Validate (including nested descriptors)
    errors = check_metadata(package, type="package")
    resources = package.get("resources", [])
    if isinstance(resources, list):
        for resource in resources:  # type: ignore
            for type in ["dialect", "schema"]:
                value = resource.get(type)  # type: ignore
                if isinstance(value, str):
                    assert_safe_path(value, basepath=basepath)
                    metadata = read_dict(value, basepath=basepath)
                    errors.extend(check_metadata(metadata, type=type))  # type: ignore

    return errors
