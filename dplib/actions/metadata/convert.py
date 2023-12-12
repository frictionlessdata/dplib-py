from __future__ import annotations

from importlib import import_module
from typing import Literal, Optional, Type, Union

from ... import types
from ...error import Error
from ...model import Model
from ...models import Package, Resource


def convert_metadata(
    path: str,
    *,
    type: IType,
    source: Optional[INotation] = None,
    target: Optional[INotation] = None,
) -> Model:
    """Convert metadata from one notation to another."""

    # Source model
    Source = Resource if type == "resource" else Package
    if source:
        module = import_module(f"dplib.plugins.{source}")
        Source: Type[Model] = getattr(module, f"{source.capitalize()}{type.capitalize()}")
    model = Source.from_path(path)
    if hasattr(model, "to_dp"):
        model = model.to_dp()

    # Target model
    Target = Resource if type == "resource" else Package
    if target:
        module = import_module(f"dplib.plugins.{target}")
        Target: Type[Model] = getattr(module, f"{target.capitalize()}{type.capitalize()}")


IType = Union[Literal["package"], Literal["resource"]]
INotation = Union[Literal["ckan"], Literal["dcat"], Literal["github"], Literal["zenodo"]]


#  def load_Resource(notation: INotation):
#  if notation == "ckan":
#  from dplib.plugins.ckan.models.resource import CkanResource

#  return CkanResource
