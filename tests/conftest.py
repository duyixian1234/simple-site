import pytest

from components.base import (make_body, make_head, make_html, make_link,
                             make_meta, make_title)


@pytest.fixture
def html_element():
    yield make_html(
        make_head(make_title("Title"), (make_meta(charset="UTF-8"), make_link("manifest", "./manifest.json"))),
        make_body(("Hello,World.",)),
    )


@pytest.fixture
def raw_html():
    yield """<html lang="en">
  <head>
    <title>
    Title
    </title>
    <meta charset="UTF-8"/>
    <link rel="manifest" href="./manifest.json"/>
  </head>
  <body>
  Hello,World.
  </body>
</html>"""
