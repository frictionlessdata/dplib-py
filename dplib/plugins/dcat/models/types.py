# SPDX-FileCopyrightText: 2024 Open Knowledge Foundation
#
# SPDX-License-Identifier: MIT

from typing import Union

from rdflib import BNode, Literal, URIRef

ISubject = Union[URIRef, BNode]
IStringNode = Union[URIRef, Literal]
