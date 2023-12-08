from __future__ import annotations

from typing import Optional

from ...model import Model
from ..profile import Profile


class Dialect(Model):
    profile: Optional[str] = None

    """A dialect description for parsing CSV files"""

    delimiter: Optional[str] = None
    """
    Specifies the character sequence which should separate fields (aka columns).
    """

    doubleQuote: Optional[bool] = None
    """
    Controls the handling of quotes inside fields.
    """

    lineTerminator: Optional[str] = None
    """
    Specifies the character sequence which should terminate rows.
    """

    quoteChar: Optional[str] = None
    """
    Specifies a one-character string to use as the quoting character.
    """

    skipInitialSpace: Optional[bool] = None
    """
    Specifies whether or not parsing will skip initial spaces after the delimiter.
    """

    header: Optional[bool] = None
    """
    Specifies whether or not the file includes a header row.
    """

    # Getters

    def get_profile(self) -> Optional[Profile]:
        if self.profile:
            return Profile.from_path(self.profile)
