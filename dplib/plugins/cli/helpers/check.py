from typing import List

from rich.console import Console
from rich.markup import escape
from rich.table import Table

from dplib.errors.metadata import MetadataError


def print_check_results(path: str, errors: List[MetadataError]):
    console = Console()
    if not errors:
        console.print(f"[bold green]Valid: {path}")
        return
    console.print(f"[bold red]Invalid: {path}", style="red")
    console.rule("[bold white]Errors", style="white")
    view = Table()
    view.add_column("location")
    view.add_column("message")
    for error in errors:
        view.add_row(escape(error.object_path), escape(error.message))
    console.print(view)
