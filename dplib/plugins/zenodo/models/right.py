from __future__ import annotations

from typing import Optional

import pydantic

from dplib.system import Model


class ZenodoRightTitle(Model):
    en: Optional[str] = None


class ZenodoRightProps(Model):
    url: Optional[str] = None
    scheme: Optional[str] = None


class ZenodoRight(Model):
    id: Optional[str] = None
    link: Optional[str] = None
    title: ZenodoRightTitle = pydantic.Field(default_factory=ZenodoRightTitle)
    props: ZenodoRightProps = pydantic.Field(default_factory=ZenodoRightProps)
