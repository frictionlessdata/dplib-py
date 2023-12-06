from typing import Optional

from rdflib import Graph, Literal, URIRef


def string(g: Graph, *, subject: URIRef, predicate: URIRef) -> Optional[str]:
    default_lang = "en"
    items = list(g.objects(subject, predicate))

    # Prefer the default language
    for item in items:
        if isinstance(item, Literal):
            if item.language and item.language == default_lang:
                return str(item)

    # Otherwise, return the first item
    if items:
        return str(items[0])
