from typing import List, Optional

from rdflib import Graph, Literal, URIRef


def id(g: Graph, *, predicate: URIRef, object: URIRef) -> Optional[URIRef]:
    try:
        id = g.value(predicate=predicate, object=object)
        if isinstance(id, URIRef):
            return id
    except Exception:
        pass


def literal(g: Graph, *, subject: URIRef, predicate: URIRef) -> Optional[Literal]:
    default_lang = "en"
    items = list(g.objects(subject, predicate))

    # Prefer the default language
    for item in items:
        if isinstance(item, Literal):
            if item.language and item.language == default_lang:
                return item

    # Otherwise, return the first item
    for item in items:
        if isinstance(item, Literal):
            return item


def string(g: Graph, *, subject: URIRef, predicate: URIRef) -> Optional[str]:
    value = literal(g, subject=subject, predicate=predicate)
    if value:
        return str(value)


def integer(g: Graph, *, subject: URIRef, predicate: URIRef) -> Optional[int]:
    value = literal(g, subject=subject, predicate=predicate)
    if value:
        return int(value)


def literals(g: Graph, *, subject: URIRef, predicate: URIRef) -> List[Literal]:
    return [item for item in g.objects(subject, predicate) if isinstance(item, Literal)]


def strings(g: Graph, *, subject: URIRef, predicate: URIRef) -> List[str]:
    return [str(item) for item in literals(g, subject=subject, predicate=predicate)]
