# SPDX-FileCopyrightText: 2024 Open Knowledge Foundation
#
# SPDX-License-Identifier: MIT

from __future__ import annotations

from dplib.system import Model


class DataciteIdentifier(Model):
    identifier: str
    identifierType: str
