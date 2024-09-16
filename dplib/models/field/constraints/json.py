# SPDX-FileCopyrightText: 2024 Open Knowledge Foundation
#
# SPDX-License-Identifier: MIT

from __future__ import annotations

from typing import Any, Dict, Optional

from .collection import CollectionConstraints


class JsonConstraints(CollectionConstraints):
    jsonSchema: Optional[Dict[str, Any]] = None
