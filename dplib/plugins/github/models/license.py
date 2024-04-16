from __future__ import annotations

from typing import Optional

from dplib.system import Model


class GithubLicense(Model):
    spdx_id: Optional[str] = None
    name: Optional[str] = None
    key: Optional[str] = None
    html_url: Optional[str] = None
