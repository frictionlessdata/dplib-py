from dplib.actions.schema.check import check_schema

from ...helpers.check import print_check_results
from ...options.path import Path
from .main import program


@program.command(name="check")
def command(
    path: Path,
):
    errors = check_schema(path)
    print_check_results(path, errors)
