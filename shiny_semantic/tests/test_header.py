import unittest

from shiny import App

from shiny_semantic import page_semantic
from shiny_semantic.elements import header, subheader


class TestHeader(unittest.TestCase):
    def test_header(self):
        expected_html_1 = '<div class="ui  header">'
        expected_html_2 = '<div class="ui huge header">'
        expected_html_3 = '<div class="ui huge icon header">'

        app = App(
            page_semantic(
                header("header"),
                header("header", class_name="huge"),
                header("header", class_name="huge icon"),
            ),
            None,
        )

        html = app.ui.get("html")

        self.assertTrue(expected_html_1 in html)
        self.assertTrue(expected_html_2 in html)
        self.assertTrue(expected_html_3 in html)

    def test_subheader(self):
        expected_html_1 = '<div class="sub header">subheader</div>'

        app = App(
            page_semantic(
                header("header", subheader("subheader"), class_name="huge"),
            ),
            None,
        )

        html = app.ui.get("html")

        self.assertTrue(expected_html_1 in html)


if __name__ == "__main__":
    unittest.main()
