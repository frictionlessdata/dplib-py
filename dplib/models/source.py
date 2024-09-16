# SPDX-FileCopyrightText: 2024 Open Knowledge Foundation
#
# SPDX-License-Identifier: MIT

from typing import Optional

from ..system import Model


class Source(Model):
    title: Optional[str] = None
    path: Optional[str] = None
    email: Optional[str] = None
    version: Optional[str] = None
