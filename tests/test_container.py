import unittest

from shiny import App

from shiny_semantic import page_semantic
from shiny_semantic.elements import container


class TestContainer(unittest.TestCase):
    def test_container(self):
        expected_html = '<div class="ui  container">'

        app = App(
            page_semantic(container("Hello")),
            None,
        )

        html = app.ui.get("html")

        self.assertTrue(expected_html in html)


if __name__ == "__main__":
    unittest.main()
