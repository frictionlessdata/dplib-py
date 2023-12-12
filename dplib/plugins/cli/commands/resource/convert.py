from typer import Option

from dplib.actions.resource.convert import convert_resource

from ...options.path import path_arg
from .main import program


@program.command(name="convert")
def command(
    path: str = path_arg,
    source: str = Option(None),
    target: str = Option(None),
):
    model = convert_resource(path, source=source, target=target)  # type: ignore
    print(model)
