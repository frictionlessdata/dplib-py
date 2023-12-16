from __future__ import annotations

from dplib.actions.package.check import check_package

from ...helpers.check import print_check_results
from ...options.path import Path
from .main import program


@program.command(name="check")
def command(
    path: str = Path,
):
    """Check the validity of a Data Package descriptor."""
    errors = check_package(path)
    print_check_results(path, errors)
