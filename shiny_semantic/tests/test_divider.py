import unittest

from shiny import App

from shiny_semantic.elements import divider


class TestDivider(unittest.TestCase):
    def test_divider(self):
        expected_html = '<div class="ui  divider">'

        element = divider("Hello")

        html = element.get_html_string()

        self.assertTrue(expected_html in html)


if __name__ == "__main__":
    unittest.main()
