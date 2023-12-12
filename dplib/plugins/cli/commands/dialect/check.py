from dplib.actions.dialect.check import check_dialect

from ...helpers.check import print_check_results
from ...options.path import Path
from .main import program


@program.command(name="check")
def command(
    path: Path,
):
    errors = check_dialect(path)
    print_check_results(path, errors)
