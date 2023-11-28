from __future__ import annotations

from typing import Optional

from ...model import Model


class GithubLicense(Model):
    key: str
    name: str
    html_url: str
    spdx_id: Optional[str] = None
