from typing import Any, Union
from urllib.parse import quote

from rdflib import Literal, URIRef


# https://github.com/ckan/ckanext-dcat/blob/master/ckanext/dcat/profiles.py
def create_node(value: Any) -> Union[URIRef, Literal]:
    try:
        stripped_value = value.strip()
        if stripped_value.startswith("http://") or stripped_value.startswith("https://"):
            # only encode this limited subset of characters to avoid more complex URL parsing
            # (e.g. valid ? in query string vs. ? as value).
            # can be applied multiple times, as encoded %xy is left untouched. Therefore, no
            # unquote is necessary beforehand.
            quotechars = " !\"$'()*,;<>[]{|}\\^`"
            for c in quotechars:
                value = value.replace(c, quote(c))
            # although all invalid chars checked by rdflib should have been quoted, try to serialize
            # the object. If it breaks, use Literal instead.
            value = URIRef(value)
            value.n3()
            # URI is fine, return the object
            return value
        else:
            return Literal(value)
    except Exception:
        # In case something goes wrong: use Literal
        return Literal(value)
