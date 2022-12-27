import unittest

from shiny import App

from shiny_semantic import page_semantic


class TestPageSemantic(unittest.TestCase):
    def test_fomantic_deps_are_present(self):
        app = App(page_semantic(), None)
        self.assertTrue("fomantic.min.css" in app.ui.get("html"))
        self.assertTrue("fomantic.min.js" in app.ui.get("html"))

    def test_shiny_bindings_are_present(self):
        app = App(page_semantic(), None)
        self.assertTrue("shiny-semantic-bindings.js" in app.ui.get("html"))


if __name__ == "__main__":
    unittest.main()
