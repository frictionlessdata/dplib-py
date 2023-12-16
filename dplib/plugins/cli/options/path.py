from __future__ import annotations

from typing import Optional

from typer import Argument, Option
from typing_extensions import Annotated

Path = Annotated[
    str,
    Argument(help="Path to the file"),
]

Format = Annotated[
    Optional[str],
    Option("--format", "-f", help="Format of the file"),
]
