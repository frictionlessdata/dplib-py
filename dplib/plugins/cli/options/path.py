from typer import Argument
from typing_extensions import Annotated

Path = Annotated[
    str,
    Argument(help="Path to the file"),
]
