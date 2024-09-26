from __future__ import annotations

import os
from pathlib import Path
from typing import Optional, Tuple

import fsspec  # type: ignore

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
    if basepath and is_file_protocol_path(basepath):
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
    if not is_file_protocol_path(path):
        return path
    if not is_file_protocol_path(basepath):
        return f"{basepath}/{path}"
    return os.path.join(basepath, path)


def is_file_protocol_path(path: str) -> bool:
    info = fsspec.utils.infer_storage_options(path)  # type: ignore
    return info.get("protocol") == "file"  # type: ignore


def is_http_or_ftp_protocol_path(path: str) -> bool:
    info = fsspec.utils.infer_storage_options(path)  # type: ignore
    return info.get("protocol") in ["http", "https", "ftp", "ftps"]  # type: ignore


def assert_safe_path(path: str, *, basepath: Optional[str] = None):
    """Assert that the path (untrusted) is not outside the basepath (trusted)"""
    if is_file_protocol_path(path):
        try:
            root = Path(basepath or os.getcwd()).resolve()
            item = root.joinpath(path).resolve()
            item.relative_to(root)
        except Exception:
            raise Error(f"Path is not safe: {path}")
