from typing import Optional

from typer import Option
from typing_extensions import Annotated

Debug = Annotated[
    Optional[bool],
    Option("--debug", "-d", help="Show debug information"),
]
