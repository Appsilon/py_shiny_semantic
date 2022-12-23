import unittest

from shiny_semantic.elements import segment


class TestSegment(unittest.TestCase):
    def test_segment(self):
        expected_html = '<div class="ui segment">'

        element = segment("Hello")
        html = element.get_html_string()

        self.assertTrue(expected_html in html)


if __name__ == "__main__":
    unittest.main()
