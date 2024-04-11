from typing import Any, Dict, Literal, Union

IData = Dict[str, Any]
IMetadataType = Union[
    Literal["package"],
    Literal["resource"],
    Literal["schema"],
    Literal["dialect"],
]
