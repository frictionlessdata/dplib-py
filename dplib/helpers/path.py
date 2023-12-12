from __future__ import annotations

import os
from pathlib import Path
from typing import Optional, Tuple
from urllib.parse import urlparse

from ..error import Error


def infer_format(path: str, *, raise_missing: bool = False):
    format = Path(path).suffix[1:]
    if format == "yml":
        format = "yaml"
    elif format == "rdf":
        format = "xml"
    if not format and raise_missing:
        raise Error(f"Cannot infer format from path: {path}")
    return format


def infer_basepath(path: str):
    basepath = os.path.dirname(path)
    if basepath and not is_remote_path(basepath):
        if not os.path.abspath(basepath):
            basepath = os.path.relpath(basepath, start=os.getcwd())
    return basepath


def ensure_basepath(path: str, basepath: Optional[str] = None) -> Tuple[str, str]:
    if basepath:
        path = join_basepath(path, basepath)
    else:
        basepath = infer_basepath(path)
    return path, basepath


def join_basepath(path: str, basepath: Optional[str] = None) -> str:
    if not basepath:
        return path
    if is_remote_path(path):
        return path
    if is_remote_path(basepath):
        return f"{basepath}/{path}"
    return os.path.join(basepath, path)


def is_remote_path(path: str) -> bool:
    path = path[0] if path and isinstance(path, list) else path
    scheme = urlparse(path).scheme
    if not scheme:
        return False
    if path.lower().startswith(scheme + ":\\"):
        return False
    return True
