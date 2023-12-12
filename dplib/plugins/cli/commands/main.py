from __future__ import annotations

from typing import Optional

import typer
from typing_extensions import Annotated

from ..program import Program
from . import dialect, package, resource, schema

program = Program()
program.add_typer(dialect.program)
program.add_typer(resource.program)
program.add_typer(package.program)
program.add_typer(schema.program)


@program.callback()
def main(
    debug: Annotated[Optional[bool], typer.Option(None, "--debug")] = None,
):
    """
    Python implementation of the Data Package standard and
    various models and utils for working with data
    """
    program.debug = debug
