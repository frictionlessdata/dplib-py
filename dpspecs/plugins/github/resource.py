from __future__ import annotations

from typing import Literal, Optional

from ...helpers.resource import path_to_name
from ...model import Model
from ...models import Resource


class GithubResource(Model):
    name: str
    path: str
    type: Literal["file"] = "file"
    content: Optional[str] = None
    encoding: Optional[str] = None
    size: Optional[int] = None
    sha: Optional[str] = None
    html_url: Optional[str] = None
    download_url: Optional[str] = None

    # Mappers

    def to_dp(self):
        resource = Resource(path=self.path, name=path_to_name(self.path))

        # General
        if self.size:
            resource.bytes = self.size
        if self.sha:
            resource.hash = f"sha1:{self.sha}"

        return resource

    def from_dp(self, resource: Resource):
        if not resource.path:
            return
        github = GithubResource(path=resource.path, name=resource.path)

        # General
        if resource.bytes:
            github.size = resource.bytes
        if resource.parsed_hash:
            if resource.parsed_hash.type == "sha1":
                github.sha = resource.parsed_hash.value

        return github
