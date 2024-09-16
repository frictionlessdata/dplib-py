# SPDX-FileCopyrightText: 2024 Open Knowledge Foundation
#
# SPDX-License-Identifier: MIT

from __future__ import annotations

from typing import Optional

from dplib.system import Model


class DataciteTitle(Model):
    title: str
    titleType: Optional[str] = None
    lang: Optional[str] = None
