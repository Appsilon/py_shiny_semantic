import unittest

from shiny import App

from shiny_semantic import page_semantic
from shiny_semantic.elements import icon


class TestIcon(unittest.TestCase):
    def test_icon(self):
        expected_html_1 = '<i class=" users icon">'
        expected_html_2 = '<i class="loading asterisk icon">'
        expected_html_3 = '<i class="large home icon">'
        expected_html_4 = '<i class="bordered teal home icon">'

        app = App(
            page_semantic(
                icon("users"),
                icon("asterisk", "loading"),
                icon("home", "large"),
                icon("home", "bordered teal"),
            ),
            None,
        )

        html = app.ui.get("html")

        self.assertTrue(expected_html_1 in html)
        self.assertTrue(expected_html_2 in html)
        self.assertTrue(expected_html_3 in html)
        self.assertTrue(expected_html_4 in html)


if __name__ == "__main__":
    unittest.main()
