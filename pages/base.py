from dataclasses import dataclass
from pathlib import Path
from typing import Callable

from html_dsl.elements import BaseHtmlElement as Element


@dataclass
class Page:
    element: Element
    path_factory: Callable[[], Path] = lambda: Path("public")

    def render(self):
        path = self.path_factory()
        parent = path.parent
        parent.mkdir(parents=True, exist_ok=True)
        path.write_text(str(self.element))
