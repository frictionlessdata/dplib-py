from __future__ import annotations

from typing import Literal, Optional

from dplib.helpers.resource import slugify_name
from dplib.models import Resource
from dplib.system import Model


class GithubResource(Model):
    """Github Resource model"""

    name: str
    path: str
    type: Literal["file"] = "file"
    content: Optional[str] = None
    encoding: Optional[str] = None
    size: Optional[int] = None
    sha: Optional[str] = None
    html_url: Optional[str] = None
    download_url: Optional[str] = None

    # Converters

    def to_dp(self) -> Resource:
        """Convert to Data Package resource

        Returns:
           Data Resource
        """
        resource = Resource(path=self.path, name=slugify_name(self.path))

        # Bytes
        if self.size:
            resource.bytes = self.size

        # Hash
        if self.sha:
            resource.hash = f"sha1:{self.sha}"

        return resource

    @classmethod
    def from_dp(cls, resource: Resource) -> Optional[GithubResource]:
        """Create Github Resource from Data Resource

        Parameters:
            resource: Data Resource

        Returns:
            Github Resource
        """
        if not resource.path or not isinstance(resource.path, str):
            return

        # Path
        github = GithubResource(path=resource.path, name=resource.path)

        # Bytes
        if resource.bytes:
            github.size = resource.bytes

        # Hash
        hash = resource.get_hash()
        if hash:
            if hash.type == "sha1":
                github.sha = hash.value

        return github
