import platform as python_platform
import sys
from functools import cached_property
from importlib import import_module
from typing import Any, Callable, ClassVar


def extras(*, name: str):
    """Extra dependency decorator"""

    def outer(func: Callable[..., Any]):
        def inner(*args: Any, **kwargs: Any):
            try:
                return func(*args, **kwargs)
            except Exception:
                module = import_module("dplib.error")
                message = f'Please install "dplib[{name}]"'
                raise module.Error(message)

        return inner

    return outer


class Platform:
    """Platform representation"""

    type: ClassVar[str] = python_platform.system().lower()
    """
    Type of the platform(OS) framework is running on. For example, windows,
    linux etc.
    """

    python: ClassVar[str] = f"{sys.version_info.major}.{sys.version_info.minor}"
    """
    Python version
    """

    # Extras

    @cached_property
    @extras(name="dcat")
    def rdflib(self):
        import rdflib

        return rdflib

    @cached_property
    @extras(name="pandas")
    def pandas(self):
        import pandas  # type: ignore

        return pandas

    @cached_property
    @extras(name="pandas")
    def pandas_core_dtypes_api(self):
        import pandas.core.dtypes.api  # type: ignore

        return pandas.core.dtypes.api

    @cached_property
    @extras(name="pandas")
    def numpy(self):
        import numpy

        return numpy

    @cached_property
    @extras(name="polars")
    def polars(self):
        import polars

        return polars

    @cached_property
    @extras(name="sql")
    def sqlalchemy(self):
        import sqlalchemy

        return sqlalchemy

    @cached_property
    @extras(name="sql")
    def sqlalchemy_exc(self):
        import sqlalchemy.exc

        return sqlalchemy.exc

    @cached_property
    @extras(name="sql")
    def sqlalchemy_schema(self):
        import sqlalchemy.schema

        return sqlalchemy.schema

    @cached_property
    @extras(name="sql")
    def sqlalchemy_dialects(self):
        import sqlalchemy.dialects

        return sqlalchemy.dialects

    @cached_property
    @extras(name="sql")
    def sqlalchemy_dialects_postgresql(self):
        import sqlalchemy.dialects.postgresql

        return sqlalchemy.dialects.postgresql

    @cached_property
    @extras(name="sql")
    def sqlalchemy_dialects_mysql(self):
        import sqlalchemy.dialects.mysql

        return sqlalchemy.dialects.mysql

    @cached_property
    @extras(name="yaml")
    def yaml(self):
        import yaml

        return yaml


platform = Platform()
