import os
import shutil
import tempfile
from pathlib import Path
from typing import Any, Optional
from urllib.parse import urlparse

import fsspec  # type: ignore

from ..error import Error


def read_file(
    path: str,
    *,
    mode: str = "rt",
    encoding: str = "utf-8",
    basepath: Optional[str] = None,
) -> str:
    try:
        path = join_basepath(path, basepath)
        with fsspec.open(path, mode=mode, encoding=encoding) as file:  # type: ignore
            return file.read()  # type: ignore
    except Exception as exception:
        raise Error(f'Cannot read file "{path}": {exception}')


def write_file(path: str, body: Any, *, mode: str = "wt", encoding: str = "utf-8"):
    try:
        eff_enc = encoding if mode == "wt" else None
        with tempfile.NamedTemporaryFile(mode, delete=False, encoding=eff_enc) as file:
            file.write(body)
            file.flush()
        move_file(file.name, path, mode=0o644)
    except Exception as exception:
        raise Error(f'Cannot write file "{path}": {exception}')


def move_file(source: str, target: str, *, mode: Optional[int] = None):
    try:
        Path(target).parent.mkdir(parents=True, exist_ok=True)
        shutil.move(source, target)
        if mode:
            os.chmod(target, 0o644)
    except Exception as exception:
        raise Error(f'Cannot move file "{source}:{target}": {exception}')


def infer_format(path: str):
    format = Path(path).suffix[1:]
    if format == "yml":
        format = "yaml"
    return format or None


def infer_basepath(path: str):
    basepath = os.path.dirname(path)
    if basepath and not is_remote_path(basepath):
        if not os.path.abspath(basepath):
            basepath = os.path.relpath(basepath, start=os.getcwd())
    return basepath


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
