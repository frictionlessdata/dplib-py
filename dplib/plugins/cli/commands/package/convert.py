from dplib.actions.package.convert import convert_package

from ...options.convert import Source, Target
from ...options.path import Path
from .main import program


@program.command(name="convert")
def command(
    path: Path,
    source: Source = None,
    target: Target = None,
):
    model = convert_package(path, source=source, target=target)  # type: ignore
    print(model)
