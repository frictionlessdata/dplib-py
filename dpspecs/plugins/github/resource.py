from __future__ import annotations

from ...model import Model
from ...models import Resource


class GithubResource(Model):
    path: str

    # Mappers

    def to_dp(self):
        return Resource(path=self.path)

    def from_dp(self, resource: Resource):
        return GithubResource(path=resource.path)
