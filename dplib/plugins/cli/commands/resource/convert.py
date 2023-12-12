from dplib.actions.resource.convert import convert_resource

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
    model = convert_resource(path, format=format, source=source, target=target)  # type: ignore
    print(model)
