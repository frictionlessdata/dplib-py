import os
from functools import lru_cache

from .file import read_file


@lru_cache
def read_profile(name: str):
    path = os.path.join(os.path.dirname(__file__), "..", "profiles", f"{name}.json")
    return read_file(path)
