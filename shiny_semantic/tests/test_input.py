import unittest

from shiny import App

from shiny_semantic import page_semantic
from shiny_semantic.elements import semantic_input


class TestInput(unittest.TestCase):
    def test_basic_input(self):
        expected_html_1 = '<div class="ui input">'
        expected_html_2 = '<input id="users" type="text" value="" placeholder=""/>'

        app = App(page_semantic(semantic_input("users")), None)

        html = app.ui.get("html")

        self.assertTrue(expected_html_1 in html)
        self.assertTrue(expected_html_2 in html)

    def test_complex_input(self):
        expected_html_3 = '<div class="ui error icon labeled input">'
        expected_html_4 = '<div class="ui label">Password</div>'
        expected_html_5 = (
            '<input id="complex" type="password"' ' value="" placeholder="Complex"/>'
        )
        expected_html_6 = '<i class=" react icon">'

        app = App(
            page_semantic(
                semantic_input(
                    input_id="complex",
                    placeholder="Complex",
                    input_type="password",
                    class_name="error",
                    icon_name="react",
                    label="Password",
                ),
            ),
            None,
        )

        html = app.ui.get("html")

        self.assertTrue(expected_html_3 in html)
        self.assertTrue(expected_html_4 in html)
        self.assertTrue(expected_html_5 in html)
        self.assertTrue(expected_html_6 in html)


if __name__ == "__main__":
    unittest.main()
