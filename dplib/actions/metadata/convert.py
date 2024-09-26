from __future__ import annotations

from importlib import import_module
from typing import List, Literal, Optional, Type, cast, get_args

from ...models import Package, Resource
from ...system import Model


def convert_metadata(
    path: str,
    *,
    type: IType,
    format: Optional[str] = None,
    source: Optional[INotation] = None,
    target: Optional[INotation] = None,
) -> Model:
    """Convert metadata from one notation to another."""

    # Validate source/target
    if source and source not in NOTATIONS:
        raise ValueError(f"Unknown source notation: {source}")
    if target and target not in NOTATIONS:
        raise ValueError(f"Unknown target notation: {target}")

    # Source model
    Source = Resource if type == "resource" else Package
    if source:
        if source not in NOTATIONS:
            raise ValueError(f"Unknown source notation: {source}")
        module = import_module(f"dplib.plugins.{source}.models")
        Source: Type[Model] = getattr(module, f"{source.capitalize()}{type.capitalize()}")
    model = Source.from_path(path, format=format)
    if source:
        model = cast(Model, model.to_dp())  # type: ignore

    # Target model
    if target:
        module = import_module(f"dplib.plugins.{target}.models")
        Target: Type[Model] = getattr(module, f"{target.capitalize()}{type.capitalize()}")
        model = cast(Model, Target.from_dp(model))  # type: ignore

    return model


IType = Literal["package", "resource"]
INotation = Literal["ckan", "dcat", "github", "zenodo"]

NOTATIONS: List[INotation] = list(get_args(INotation))
