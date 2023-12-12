from typer import Option

from dplib.actions.package.convert import convert_package

from ...options.path import path_arg
from .main import program


@program.command(name="convert")
def command(
    path: str = path_arg,
    source: str = Option(None, "--source", "-s", help="Source notation e.g. ckan"),
    target: str = Option(None, "--target", "-t", help="Target notation e.g. dcat"),
):
    model = convert_package(path, source=source, target=target)  # type: ignore
    print(model)
