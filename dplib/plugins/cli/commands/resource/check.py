from dplib.actions.resource.check import check_resource

from ...helpers.check import print_check_results
from ...options.path import Path
from .main import program


@program.command(name="check")
def command(
    path: Path,
):
    errors = check_resource(path)
    print_check_results(path, errors)