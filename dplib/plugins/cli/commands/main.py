from __future__ import annotations

from ..options.system import Debug
from ..program import Program
from . import dialect, package, resource, schema

program = Program()
program.add_typer(dialect.program)
program.add_typer(resource.program)
program.add_typer(package.program)
program.add_typer(schema.program)


@program.callback()
def main(
    debug: bool = Debug,
):
    """
    Python implementation of the Data Package standard and
    various tools for working with data
    """
    program.debug = debug
