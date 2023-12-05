from __future__ import annotations

from ...model import Model


class ParsedHash(Model):
    type: str
    value: str

    @property
    def hash(self):
        return self.value if self.type == "md5" else self.full_hash

    @property
    def full_hash(self):
        return f"{self.type}:{self.value}"

    @classmethod
    def from_hash(cls, hash: str) -> ParsedHash:
        parts = hash.split(":", maxsplit=1)
        if len(parts) == 1:
            return ParsedHash(type="md5", value=parts[0])
        return ParsedHash(type=parts[0], value=parts[1])
