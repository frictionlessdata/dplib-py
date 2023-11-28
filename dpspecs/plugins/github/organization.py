from __future__ import annotations

from ...model import Model


class GithubOrganization(Model):
    login: str
    html_url: str
