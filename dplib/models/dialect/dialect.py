from __future__ import annotations

from typing import Optional

from ...model import Model
from ..profile import Profile


class Dialect(Model):
    """Table Dialect model"""

    profile: Optional[str] = None

    """A dialect description for parsing CSV files"""

    title: Optional[str] = None
    """
    A string providing a title or one sentence description for this dialect
    """

    description: Optional[str] = None
    """
    A description of the dialect. The description MUST be markdown formatted —
    this also allows for simple plain text as plain text is itself valid markdown.
    """

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
        """Get the resovled profile of the dialect

        Returns:
            The resolved profile of the dialect
        """
        if self.profile:
            return Profile.from_path(self.profile)

    def get_delimiter(self) -> str:
        """Get the delimiter of the dialect

        Returns:
            Provided delimiter or default delimiter
        """
        return self.delimiter if self.delimiter is not None else ","

    def get_line_terminator(self) -> str:
        """Get the line terminator of the dialect

        Returns:
            Provided line terminator or default line terminator
        """
        return self.lineTerminator if self.lineTerminator is not None else "\r\n"

    def get_quote_char(self) -> str:
        """Get the quote character of the dialect

        Returns:
            Provided quote character or default quote character
        """
        return self.quoteChar if self.quoteChar is not None else '"'

    def get_double_quote(self) -> bool:
        """Get the double quote of the dialect

        Returns:
            Provided double quote or default double quote
        """
        return self.doubleQuote if self.doubleQuote is not None else True

    def get_header(self) -> bool:
        """Get the header flag of the dialect

        Returns:
            Provided header flag or default header flag
        """
        return self.header if self.header is not None else True
