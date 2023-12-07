from typing import Any

from rdflib import Graph, URIRef

from .helpers import create_node
from .types import ISubject


def id(g: Graph, identifier: str, *, predicate: URIRef, object: URIRef):
    subject = URIRef(identifier)
    g.add((subject, predicate, object))
    return subject


def node(g: Graph, value: Any, *, subject: ISubject, predicate: URIRef):
    object = create_node(value)
    g.add((subject, predicate, object))
