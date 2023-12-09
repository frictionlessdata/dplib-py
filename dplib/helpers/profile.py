import os
from functools import lru_cache

from ..error import Error
from .data import load_data
from .file import read_file


@lru_cache
def read_profile(name: str):
    format = "json"
    path = os.path.join(os.path.dirname(__file__), "..", "profiles", f"{name}.{format}")
    try:
        text = read_file(path)
    except Exception:
        raise Error(f'Cannot read profile "{name}" at "{path}"')
    data = load_data(text, format=format)
    return data
