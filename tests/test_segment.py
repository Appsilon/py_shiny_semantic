import unittest

from shiny import App

from shiny_semantic import page_semantic
from shiny_semantic.elements import segment


class TestSegment(unittest.TestCase):
    def test_segment(self):
        expected_html = '<div class="ui  segment">'

        app = App(
            page_semantic(segment("Hello")),
            None,
        )

        html = app.ui.get("html")

        self.assertTrue(expected_html in html)


if __name__ == "__main__":
    unittest.main()
