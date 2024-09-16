# SPDX-FileCopyrightText: 2024 Open Knowledge Foundation
#
# SPDX-License-Identifier: MIT

from __future__ import annotations

from typer import Argument, Option

Path = Argument(help="Path to the file")
Format = Option(None, "--format", "-f", help="Format of the file")
