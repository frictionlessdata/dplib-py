from ...model import Model


class ParsedHash(Model):
    type: str
    value: str

    @property
    def notation(self):
        return f"{self.type}:{self.value}"
