from __future__ import annotations

from pathlib import Path

from slugify import slugify


def slugify_name(name: str) -> str:
    return slugify(Path(name).stem, separator="_")
