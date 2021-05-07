from typing import Optional, Tuple

from html_dsl.elements import BaseHtmlElement as Element


def make_html(head: Element, body: Element, language: str = "en") -> Element:
    element = Element("html")
    return element(lang=language)[head, body]


def make_head(title: Element, metas: Tuple) -> Element:
    return Element("head")[(title, *metas)]


def make_meta(**kwargs) -> Element:
    return Element("meta", no_content=True)(**kwargs)


def make_link(rel: str, href: str, *, _type: Optional[str] = None) -> Element:
    kwargs = dict(rel=rel, href=href)
    if _type:
        kwargs["type"] = _type
    return Element("link", no_content=True)(**kwargs)


def make_title(text: str) -> Element:
    return Element("title")[text]


def make_script(*, src: Optional[str] = None, _type: Optional[str] = None, content: str = "") -> Element:
    element = Element("script")
    kwargs = {}
    if src:
        kwargs["src"] = src
    if _type:
        kwargs["type"] = _type
    element = element(**kwargs)
    return element[content]


def make_body(children: Tuple[Element]) -> Element:
    return Element("body")[children]
