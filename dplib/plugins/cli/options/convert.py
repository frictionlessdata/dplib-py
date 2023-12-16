from __future__ import annotations

from typing import Optional

from typer import Option
from typing_extensions import Annotated

Source = Annotated[
    Optional[str],
    Option("--source", "-s", help="Source notation e.g. ckan"),
]

Target = Annotated[
    Optional[str],
    Option("--target", "-t", help="Target notation e.g. dcat"),
]
