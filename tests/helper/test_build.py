from pathlib import Path

from helper import build
from pages.base import Page
from pages.index import element


def test_find_pages():
    assert build.find_pages()


def test_build(tmp_path: Path):
    page = Page(element, lambda: tmp_path / "index.html")
    build.build_pages([page])
    assert (tmp_path / "index.html").read_text() == str(page.element)


def test_clean(tmp_path: Path):
    path = tmp_path / "public"
    path.mkdir()
    build.clean_build(path)
    assert not path.exists()
