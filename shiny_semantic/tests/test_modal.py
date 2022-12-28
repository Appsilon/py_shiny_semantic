import unittest

from shiny_semantic.modules import modal

# Most important functionality can be tested only in a reactive environment


class TestModal(unittest.TestCase):
    def test_modal(self):
        expected_html_1 = '<div id="modal" class="ui modal">'
        expected_html_2 = '<div class="header">Header</div>'
        expected_html_3 = '<div class="content">Content</div>'
        expected_html_4 = '<div class="actions">'

        # Expect default buttons, but their default classes are prone to change
        expected_html_5 = '<button id="cancel"'
        expected_html_6 = '<button id="ok"'

        element = modal(
            id="modal",
            header="Header",
            content="Content",
            actions=None,
        )

        html = element.get_html_string()

        self.assertTrue(expected_html_1 in html)
        self.assertTrue(expected_html_2 in html)
        self.assertTrue(expected_html_3 in html)
        self.assertTrue(expected_html_4 in html)
        self.assertTrue(expected_html_5 in html)
        self.assertTrue(expected_html_6 in html)


if __name__ == "__main__":
    unittest.main()
