from __future__ import annotations

import sys
from typing import Any, Optional

import typer
from rich.console import Console
from rich.markup import escape


class Program(typer.Typer):
    debug: Optional[bool] = False

    def __call__(self, *args: Any, **kwargs: Any):
        try:
            super().__call__(*args, **kwargs)
        except Exception as exception:
            try:
                if self.debug:
                    raise
                console = Console()
                console.print(escape(str(exception)), style="bold red")
                raise typer.Exit(code=1)
            except typer.Exit as e:
                sys.exit(e.exit_code)
            except KeyError:
                raise
