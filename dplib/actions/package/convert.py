from typing import Optional

from ...system import Model
from ..metadata.convert import INotation, convert_metadata


def convert_package(
    path: str,
    *,
    format: Optional[str] = None,
    source: Optional[INotation] = None,
    target: Optional[INotation] = None,
) -> Model:
    """Convert a Data Package descriptor from one notation to another

    Parameters:
        path: Path to the descriptor
        format: Format of the descriptor
        source: Source notation e.g. ckan (default dp)
        target: Target notation e.g. dcat (default dp)

    Returns:
        Package model
    """
    return convert_metadata(
        path, type="package", format=format, source=source, target=target
    )
