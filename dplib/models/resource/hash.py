from __future__ import annotations

from pydantic import BaseModel
from typing_extensions import Self


class Hash(BaseModel):
    type: str
    value: str

    @property
    def short(self):
        return self.value if self.type == "md5" else self.long

    @property
    def long(self):
        return f"{self.type}:{self.value}"

    # Converters

    @classmethod
    def from_text(cls, text: str) -> Self:
        parts = text.split(":", maxsplit=1)
        if len(parts) == 1:
            return cls(type="md5", value=parts[0])
        return cls(type=parts[0], value=parts[1])
