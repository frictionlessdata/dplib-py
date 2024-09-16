# SPDX-FileCopyrightText: 2024 Open Knowledge Foundation
#
# SPDX-License-Identifier: MIT

from __future__ import annotations

from dplib import settings

from .main import program


@program.command(name="version", help="Print the version of the program.")
def command():
    print(settings.VERSION)
