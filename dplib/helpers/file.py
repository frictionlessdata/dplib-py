from __future__ import annotations

import os
import shutil
import tempfile
from pathlib import Path
from typing import Any, Optional

import fsspec  # type: ignore

from ..error import Error
from .path import join_basepath


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
    except Exception:
        raise Error(f'Cannot read file "{path}"')


def write_file(
    path: str,
    body: Any,
    *,
    mode: str = "wt",
    encoding: str = "utf-8",
    permissions: int = 0o600,
):
    try:
        eff_enc = encoding if mode == "wt" else None
        with tempfile.NamedTemporaryFile(mode, delete=False, encoding=eff_enc) as file:
            file.write(body)
            file.flush()
        move_file(file.name, path, permissions=permissions)
    except Exception:
        raise Error(f'Cannot write file "{path}"')


def move_file(source: str, target: str, *, permissions: int = 0o600):
    try:
        Path(target).parent.mkdir(parents=True, exist_ok=True)
        shutil.move(source, target)
        os.chmod(target, permissions)
    except Exception:
        raise Error(f'Cannot move file "{source}:{target}"')
