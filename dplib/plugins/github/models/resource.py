from __future__ import annotations

from typing import Literal, Optional

from dplib.helpers.resource import path_to_name
from dplib.model import Model
from dplib.models import Resource


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

        # Bytes
        if self.size:
            resource.bytes = self.size

        # Hash
        if self.sha:
            resource.hash = f"sha1:{self.sha}"

        return resource

    @classmethod
    def from_dp(cls, resource: Resource) -> Optional[GithubResource]:
        if not resource.path:
            return

        # Path
        github = GithubResource(path=resource.path, name=resource.path)

        # Bytes
        if resource.bytes:
            github.size = resource.bytes

        # Hash
        if resource.parsed_hash:
            if resource.parsed_hash.type == "sha1":
                github.sha = resource.parsed_hash.value

        return github
