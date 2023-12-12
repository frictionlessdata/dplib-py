from __future__ import annotations

from importlib import import_module
from typing import Literal, Optional, Type, Union, cast

from ...model import Model
from ...models import Package, Resource


def convert_metadata(
    path: str,
    *,
    type: IType,
    format: Optional[str] = None,
    source: Optional[INotation] = None,
    target: Optional[INotation] = None,
) -> Model:
    """Convert metadata from one notation to another."""

    # Source model
    Source = Resource if type == "resource" else Package
    if source:
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


IType = Union[Literal["package"], Literal["resource"]]
INotation = Union[Literal["ckan"], Literal["dcat"], Literal["github"], Literal["zenodo"]]
