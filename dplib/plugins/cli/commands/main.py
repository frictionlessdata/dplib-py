from __future__ import annotations

from typing import Optional

import typer

from dplib import settings

from .schema import program_schema

program = typer.Typer()
program.add_typer(program_schema)


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
