from typer import Option
from typing_extensions import Annotated

Debug = Annotated[
    bool,
    Option(False, "--debug", "-d", help="Show debug information"),
]
