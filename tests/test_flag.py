import unittest

from shiny import App

from shiny_semantic import page_semantic
from shiny_semantic.elements import flag


class TestFlag(unittest.TestCase):
    def test_flag(self):
        expected_html_1 = '<i class=" france flag">'
        expected_html_2 = '<i class=" fr flag">'
        expected_html_3 = '<i class="big fr flag">'

        app = App(
            page_semantic(
                flag("france"),
                flag("fr"),
                flag("fr", class_name="big"),
            ),
            None,
        )

        html = app.ui.get("html")

        self.assertTrue(expected_html_1 in html)
        self.assertTrue(expected_html_2 in html)
        self.assertTrue(expected_html_3 in html)


if __name__ == "__main__":
    unittest.main()
