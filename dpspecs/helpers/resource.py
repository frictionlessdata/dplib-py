from pathlib import Path

from slugify import slugify


def path_to_name(path: str) -> str:
    return slugify(Path(path).stem, separator="_")
