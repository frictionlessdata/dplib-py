from dplib.actions.schema.check import check_schema

from ...helpers.check import print_check_results
from ...options.path import path_arg
from .main import program_schema


@program_schema.command(name="check")
def program_schema_check(
    path: str = path_arg,
):
    errors = check_schema(path)
    print_check_results(path, errors)
