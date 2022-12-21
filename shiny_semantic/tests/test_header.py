import unittest

from htmltools import TagList

from shiny_semantic.elements import header, subheader


class TestHeader(unittest.TestCase):
    def test_header(self):
        expected_html_1 = '<div class="ui  header">'
        expected_html_2 = '<div class="ui huge header">'
        expected_html_3 = '<div class="ui huge icon header">'

        elements = TagList(
            header("header"),
            header("header", class_name="huge"),
            header("header", class_name="huge icon"),
        )

        html = elements.get_html_string()

        self.assertTrue(expected_html_1 in html)
        self.assertTrue(expected_html_2 in html)
        self.assertTrue(expected_html_3 in html)

    def test_subheader(self):
        expected_html_1 = '<div class="sub header">subheader</div>'

        element = header("header", subheader("subheader"), class_name="huge")

        html = element.get_html_string()

        self.assertTrue(expected_html_1 in html)


if __name__ == "__main__":
    unittest.main()
