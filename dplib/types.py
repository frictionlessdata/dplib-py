from typing import Any, Dict, Literal, Union

IDict = Dict[str, Any]
IMetadataType = Union[
    Literal["package"],
    Literal["resource"],
    Literal["schema"],
    Literal["dialect"],
]
