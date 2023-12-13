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

    lineTerminator: Optional[str] = None
    """
    Specifies the character sequence which should terminate rows.
    """

    quoteChar: Optional[str] = None
    """
    Specifies a one-character string to use as the quoting character.
    """

    doubleQuote: Optional[bool] = None
    """
    Controls the handling of quotes inside fields.
    """

    escapeChar: Optional[str] = None
    """
    Specifies a one-character string to use as the escape character.
    """

    nullSequence: Optional[str] = None
    """
    Specifies the character sequence which represents a null value.
    """

    skipInitialSpace: Optional[bool] = None
    """
    Specifies whether or not parsing will skip initial spaces after the delimiter.
    """

    header: Optional[bool] = None
    """
    Specifies whether or not the file includes a header row.
    """

    commentChar: Optional[str] = None
    """
    Specifies a one-character string to use as the comment character.
    """

    # Getters

    def get_profile(self) -> Optional[Profile]:
        if self.profile:
            return Profile.from_path(self.profile)

    def get_delimiter(self) -> str:
        return self.delimiter if self.delimiter is not None else ","

    def get_line_terminator(self) -> str:
        return self.lineTerminator if self.lineTerminator is not None else "\r\n"

    def get_quote_char(self) -> str:
        return self.quoteChar if self.quoteChar is not None else '"'

    def get_double_quote(self) -> bool:
        return self.doubleQuote if self.doubleQuote is not None else True

    def get_header(self) -> bool:
        return self.header if self.header is not None else True
