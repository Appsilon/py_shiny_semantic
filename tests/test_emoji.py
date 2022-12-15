import unittest

from shiny import App

from shiny_semantic import page_semantic
from shiny_semantic.elements import emoji


class TestEmoji(unittest.TestCase):
    def test_emoji(self):
        test_case_1 = '<em data-emoji=":adult:" class="medium">'
        test_case_2 = '<em data-emoji=":adult:" class="big">'

        app = App(
            page_semantic(
                emoji("adult"),
                emoji("adult", class_name="big"),
            ),
            None,
        )

        html = app.ui.get("html")

        self.assertTrue(test_case_1 in html)
        self.assertTrue(test_case_2 in html)


if __name__ == "__main__":
    unittest.main()
