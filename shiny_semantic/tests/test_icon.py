import unittest

from htmltools import TagList

from shiny_semantic.elements import icon


class TestIcon(unittest.TestCase):
    def test_icon(self):
        expected_html_1 = '<i class=" users icon">'
        expected_html_2 = '<i class="loading asterisk icon">'
        expected_html_3 = '<i class="large home icon">'
        expected_html_4 = '<i class="bordered teal home icon">'

        elements = TagList(
            icon("users"),
            icon("asterisk", "loading"),
            icon("home", "large"),
            icon("home", "bordered teal"),
        )

        html = elements.get_html_string()

        self.assertTrue(expected_html_1 in html)
        self.assertTrue(expected_html_2 in html)
        self.assertTrue(expected_html_3 in html)
        self.assertTrue(expected_html_4 in html)


if __name__ == "__main__":
    unittest.main()
