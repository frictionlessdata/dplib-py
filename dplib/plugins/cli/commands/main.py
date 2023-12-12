from __future__ import annotations

from typing import Optional

import typer

from dplib import settings

from ..program import Program
from . import dialect, package, resource, schema

program = Program()
program.add_typer(dialect.program)
program.add_typer(resource.program)
program.add_typer(package.program)
program.add_typer(schema.program)


# Helpers


def version(value: bool):
    if value:
        typer.echo(settings.VERSION)
        raise typer.Exit()


# Command


@program.callback()
def program_main(
    version: Optional[bool] = typer.Option(None, "--version", callback=version),
):
    """
    Python implementation of the Data Package standard and
    various models and utils for working with data
    """
    pass
