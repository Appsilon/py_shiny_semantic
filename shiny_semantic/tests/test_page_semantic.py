import unittest

from shiny import App

from shiny_semantic import page_semantic


class TestPageSemantic(unittest.TestCase):
    def test_fomantic_deps_are_present(self):
        app = App(page_semantic(), None)
        html = app.ui.get("html")
        self.assertTrue("fomantic.min.css" in html)
        self.assertTrue("fomantic.min.js" in html)
        self.assertTrue("shiny-semantic-bindings.js" in html)


if __name__ == "__main__":
    unittest.main()
