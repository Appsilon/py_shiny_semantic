import unittest

from htmltools import TagList

from shiny_semantic.elements import emoji


class TestEmoji(unittest.TestCase):
    def test_emoji(self):
        test_case_1 = '<em data-emoji=":adult:">'
        test_case_2 = '<em data-emoji=":adult:" class="big">'

        elements = TagList(
            emoji("adult"),
            emoji("adult", class_name="big"),
        )

        html = elements.get_html_string()

        self.assertTrue(test_case_1 in html)
        self.assertTrue(test_case_2 in html)


if __name__ == "__main__":
    unittest.main()
