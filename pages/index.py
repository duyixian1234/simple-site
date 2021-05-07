from pathlib import Path

from components.base import (make_body, make_head, make_html, make_link,
                             make_meta, make_title)

from .base import Page

element = make_html(
    make_head(
        make_title("Title"),
        (
            make_meta(charset="UTF-8"),
            make_link("manifest", "./manifest.json"),
        ),
    ),
    make_body(("Hello,World.",)),
)

path = Path("public") / "index.html"

index = Page(element, path)
