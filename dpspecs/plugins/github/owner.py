from __future__ import annotations

from ...model import Model


class GithubOwner(Model):
    login: str
    html_url: str
