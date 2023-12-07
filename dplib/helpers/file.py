import os
import shutil
import tempfile
from pathlib import Path
from typing import Any, Optional

import fsspec  # type: ignore

from ..error import Error


def read_file(path: str, *, mode: str = "rt", encoding: str = "utf-8") -> str:
    try:
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
