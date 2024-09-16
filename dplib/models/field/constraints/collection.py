# SPDX-FileCopyrightText: 2024 Open Knowledge Foundation
#
# SPDX-License-Identifier: MIT

from __future__ import annotations

from typing import Optional

from .base import BaseConstraints


class CollectionConstraints(BaseConstraints[str]):
    minLength: Optional[int] = None
    maxLength: Optional[int] = None
