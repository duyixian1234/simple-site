from dataclasses import dataclass
from pathlib import Path

from html_dsl.elements import BaseHtmlElement as Element


@dataclass
class Page:
    element: Element
    path: Path

    def render(self):
        parent = self.path.parent
        parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text(str(self.element))
