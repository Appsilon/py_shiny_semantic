import unittest

from shiny_semantic.elements import container


class TestContainer(unittest.TestCase):
    def test_container(self):
        expected_html = '<div class="ui container">'

        element = container("Hello")

        html = element.get_html_string()

        self.assertTrue(expected_html in html)


if __name__ == "__main__":
    unittest.main()
