from dplib.actions.package.convert import convert_package

from ...options.convert import Source, Target
from ...options.path import Format, Path
from .main import program


@program.command(name="convert")
def command(
    path: Path,
    format: Format = None,
    source: Source = None,
    target: Target = None,
):
    model = convert_package(path, format=format, source=source, target=target)  # type: ignore
    print(model)
