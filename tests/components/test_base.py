from html_dsl.elements import BaseHtmlElement as Element

from components.base import make_body, make_head, make_link, make_meta, make_script, make_title


def assert_equal(element: Element, raw: str) -> None:
    assert str(element) == raw


def test_html(html_element: Element, raw_html: str):
    assert_equal(html_element, raw_html)


def test_title():
    element = make_title("Title")
    expect = "<title>\nTitle\n</title>"
    assert_equal(element, expect)


def test_head():
    element = make_head(make_title("Title"), tuple())
    expect = "<head>\n  <title>\n  Title\n  </title>\n</head>"
    assert_equal(element, expect)


def test_meta():
    expect = '<meta charset="UTF-8"/>'
    element = make_meta(charset="UTF-8")
    assert_equal(element, expect)


def test_link():
    expect = '<link rel="manifest" href="./manifest.json"/>'
    element = make_link("manifest", "./manifest.json")
    assert_equal(element, expect)

    expect = '<link rel="icon" href="./img/icons/64x64.png" type="image/png"/>'
    element = make_link("icon", "./img/icons/64x64.png", _type="image/png")
    assert_equal(element, expect)


def test_script():
    expect = '<script src="./bundle.js">\n\n</script>'
    element = make_script(src="./bundle.js")
    assert_equal(element, expect)

    expect = '<script type="javascript">\nconsole.log("loaded");\n</script>'
    element = make_script(_type="javascript", content='console.log("loaded");')
    assert_equal(element, expect)


def test_body():
    expect = "<body>\n\n</body>"
    element = make_body(tuple())
    assert_equal(element, expect)
