from __future__ import annotations

from typing import List, Optional

import pydantic

from ...model import Model
from ..contributor import Contributor
from ..license import License
from ..profile import Profile
from ..resource import Resource
from ..source import Source


class Package(Model):
    basepath: Optional[str] = pydantic.Field(default=None, exclude=True)

    id: Optional[str] = None
    name: Optional[str] = None
    profile: Optional[str] = None
    resources: List[Resource] = []

    title: Optional[str] = None
    description: Optional[str] = None
    homepage: Optional[str] = None
    version: Optional[str] = None
    licenses: List[License] = []
    sources: List[Source] = []
    contributors: List[Contributor] = []
    keywords: List[str] = []
    image: Optional[str] = None
    created: Optional[str] = None

    def model_post_init(self, _):
        for resource in self.resources:
            resource.basepath = self.basepath

    # Getters

    def get_profile(self) -> Optional[Profile]:
        if self.profile:
            return Profile.from_path(self.profile)

    def get_resource(
        self, *, name: Optional[str] = None, path: Optional[str] = None
    ) -> Optional[Resource]:
        for resource in self.resources:
            if name and resource.name == name:
                return resource
            if path and resource.path == path:
                return resource

    # Setters

    def add_resource(self, resource: Resource) -> None:
        resource.basepath = self.basepath
        self.resources.append(resource)

    # Methods

    def dereference(self):
        for resource in self.resources:
            resource.dereference()
