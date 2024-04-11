from __future__ import annotations

from typing import List, Optional

from ...model import Model
from ..profile import Profile
from .types import IItemType


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

    # General

    header: bool = True
    """
    Specifies whether or not the file includes a header row.
    """

    headerRows: List[int] = []
    """
    This property specifies the row numbers for the header.
    """

    headerJoin: str = " "
    """
    This property specifies how multiline-header files
    have to join the resulting header rows.
    """

    commentRows: List[int] = []
    """
    This property specifies what rows have to be omitted from the data.
    """

    commentChar: Optional[str] = None
    """
    Specifies a one-character string to use as the comment character.
    """

    # Delimited

    delimiter: str = ","
    """
    Specifies the character sequence which should separate fields (aka columns).
    """

    lineTerminator: str = "\r\n"
    """
    Specifies the character sequence which should terminate rows.
    """

    quoteChar: str = '"'
    """
    Specifies a one-character string to use as the quoting character.
    """

    doubleQuote: bool = True
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

    # Structured

    property: Optional[str] = None
    """
    This property specifies where a data array is located in the data structure.
    """

    itemType: Optional[IItemType] = None
    """
    This property specifies whether the data property contains
    an array of arrays or an array of objects.
    """

    itemKeys: List[str] = []
    """
    This property specifies the way of extracting rows
    from data arrays with itemType is object.
    """

    # Spreadsheet

    sheetNumber: int = 1
    """
    This property specifies a sheet number of a table in the spreadsheet file.
    """

    sheetName: Optional[str] = None
    """
    This property specifies a sheet name of a table in the spreadsheet file.
    """

    # Getters

    def get_profile(self) -> Optional[Profile]:
        """Get the resovled profile of the dialect

        Returns:
            The resolved profile of the dialect
        """
        if self.profile:
            return Profile.from_path(self.profile)
