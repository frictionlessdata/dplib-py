from __future__ import annotations

from typing import Optional

from rich.console import Console

from dplib.actions.resource.convert import convert_resource

from ...options.convert import Source, Target
from ...options.path import Format, Path
from .main import program


@program.command(name="convert")
def command(
    path: str = Path,
    format: Optional[str] = Format,
    source: Optional[str] = Source,
    target: Optional[str] = Target,
):
    """Convert a Data Resource descriptor from one notation to another."""
    console = Console()
    model = convert_resource(path, format=format, source=source, target=target)  # type: ignore
    console.print_json(model.to_text(format="json"))
