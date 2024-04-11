from __future__ import annotations

from typing import Literal, Union

IFieldType = Union[
    Literal["any"],
    Literal["array"],
    Literal["boolean"],
    Literal["date"],
    Literal["datetime"],
    Literal["duration"],
    Literal["geojson"],
    Literal["geopoint"],
    Literal["integer"],
    Literal["list"],
    Literal["number"],
    Literal["object"],
    Literal["string"],
    Literal["time"],
    Literal["year"],
    Literal["yearmonth"],
]

IItemType = Union[
    Literal["boolean"],
    Literal["date"],
    Literal["datetime"],
    Literal["integer"],
    Literal["number"],
    Literal["string"],
    Literal["time"],
]
