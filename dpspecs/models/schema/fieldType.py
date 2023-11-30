from __future__ import annotations

from typing import Literal, Union

FieldType = Union[
    Literal["any"],
    Literal["array"],
    Literal["boolean"],
    Literal["date"],
    Literal["datetime"],
    Literal["duration"],
    Literal["geojson"],
    Literal["geopoint"],
    Literal["integer"],
    Literal["number"],
    Literal["object"],
    Literal["string"],
    Literal["time"],
    Literal["year"],
    Literal["yearmonth"],
]
