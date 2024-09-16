# SPDX-FileCopyrightText: 2024 Open Knowledge Foundation
#
# SPDX-License-Identifier: MIT

from __future__ import annotations

from typing import Optional

from dplib.system import Model


class DataciteDescription(Model):
    description: str
    descriptionType: str
    lang: Optional[str] = None
