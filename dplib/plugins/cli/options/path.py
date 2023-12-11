from typer import Argument

path_arg = Argument(
    default=None,
    help="Data source [default: stdin]",
)
