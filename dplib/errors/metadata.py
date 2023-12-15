from __future__ import annotations

import re

from jsonschema.exceptions import ValidationError

from ..error import Error


class MetadataError(Error):
    source: ValidationError
    message: str
    schema_path: str
    object_path: str
    full_message: str

    def __init__(self, source: ValidationError):
        self.source = source
        self.schema_path = "/" + "/".join(map(str, source.schema_path))
        self.object_path = "/" + "/".join(map(str, source.path))
        self.message = re.sub(r"\s+", " ", source.message)
        self.full_message = self.message
        if self.object_path:
            self.full_message = f"[{self.object_path}] {self.message}"
        super().__init__(self.full_message)
