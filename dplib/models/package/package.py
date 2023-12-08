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

    basepath: Optional[str] = pydantic.Field(default=None, exclude=True)

    # Getters

    def get_profile(self) -> Optional[Profile]:
        if self.profile:
            return Profile.from_path(self.profile)
