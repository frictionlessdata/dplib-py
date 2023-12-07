from typing import List, Optional

from rdflib import Graph, Literal, URIRef

from .types import IStringNode, ISubject


def id(g: Graph, *, predicate: URIRef, object: URIRef) -> Optional[URIRef]:
    try:
        id = g.value(predicate=predicate, object=object)
        if isinstance(id, URIRef):
            return id
    except Exception:
        pass


def node(g: Graph, *, subject: ISubject, predicate: URIRef) -> Optional[IStringNode]:
    default_lang = "en"
    items = list(g.objects(subject, predicate))

    # Prefer the default language
    for item in items:
        if isinstance(item, Literal):
            if item.language and item.language == default_lang:
                return item

    # Otherwise, return the first item
    for item in items:
        if isinstance(item, (URIRef, Literal)):
            return item


def string(g: Graph, *, subject: ISubject, predicate: URIRef) -> Optional[str]:
    value = node(g, subject=subject, predicate=predicate)
    if value:
        return str(value)


def integer(g: Graph, *, subject: ISubject, predicate: URIRef) -> Optional[int]:
    value = node(g, subject=subject, predicate=predicate)
    if value:
        try:
            return int(value)
        except Exception:
            pass


def nodes(g: Graph, *, subject: ISubject, predicate: URIRef) -> List[IStringNode]:
    return [
        item
        for item in g.objects(subject, predicate)
        if isinstance(item, (URIRef, Literal))
    ]


def strings(g: Graph, *, subject: ISubject, predicate: URIRef) -> List[str]:
    return [str(item) for item in nodes(g, subject=subject, predicate=predicate)]
