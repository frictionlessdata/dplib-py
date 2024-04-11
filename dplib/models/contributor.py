from typing import List, Optional

from ..model import Model


class Contributor(Model):
    title: Optional[str] = None
    givenName: Optional[str] = None
    familyName: Optional[str] = None
    path: Optional[str] = None
    email: Optional[str] = None
    roles: Optional[List[str]] = []
    organization: Optional[str] = None

    def model_post_init(self, _):
        # contributor.role (standards/v1)
        if not self.roles:
            role = self.custom.pop("role", None)
            if role:
                self.roles = [role]
