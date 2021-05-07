from pathlib import Path

from html_dsl.elements import BaseHtmlElement as Element

from pages.base import Page


def test_page(html_element: Element, raw_html: str, tmp_path: Path):
    index = tmp_path / "index.html"
    page = Page(html_element, lambda: index)
    page.render()
    assert index.read_text() == raw_html
