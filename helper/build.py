import importlib
from concurrent.futures.thread import ThreadPoolExecutor
from typing import List

from pages.base import Page


def find_pages() -> List[Page]:
    module = importlib.import_module("pages")
    pages = []
    for name in dir(module):
        attr = getattr(module, name)
        if isinstance(attr, Page):
            pages.append(attr)
    return pages


def build_pages(pages: List[Page]):
    with ThreadPoolExecutor() as executor:
        list(executor.map(Page.render, pages))
