import unittest

from shiny import App

from shiny_semantic import page_semantic
from shiny_semantic.elements import divider


class TestDivider(unittest.TestCase):
    def test_divider(self):
        expected_html = '<div class="ui  divider">'

        app = App(
            page_semantic(divider("Hello")),
            None,
        )

        html = app.ui.get("html")

        self.assertTrue(expected_html in html)


if __name__ == "__main__":
    unittest.main()
