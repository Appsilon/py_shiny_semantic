import unittest

from shiny_semantic.elements import icon, semantic_input


class TestInput(unittest.TestCase):
    def test_basic_input(self):
        expected_html_1 = '<div class="ui input">'
        expected_html_2 = '<input id="users" type="text" value="" placeholder=""/>'

        element = semantic_input("users")

        html = element.get_html_string()

        self.assertTrue(expected_html_1 in html)
        self.assertTrue(expected_html_2 in html)

    def test_complex_input(self):
        expected_html_3 = '<div class="ui error icon labeled input">'
        expected_html_4 = '<div class="ui label">Password</div>'
        expected_html_5 = '<input id="complex" type="password" value="" placeholder="Complex"/>'
        expected_html_6 = '<i class="react icon">'

        element = semantic_input(
            id="complex",
            placeholder="Complex",
            type="password",
            icon=icon("react"),
            semantic_class="error",
            semantic_label="Password",
        )

        html = element.get_html_string()

        self.assertTrue(expected_html_3 in html)
        self.assertTrue(expected_html_4 in html)
        self.assertTrue(expected_html_5 in html)
        self.assertTrue(expected_html_6 in html)

    def test_custom_label(self):
        expected_html = (
            '<div class="ui labeled input">\n'
            '  <div class="ui orange label">hello</div>\n'
            '  <input id="custom_label" type="text" value="world" placeholder=""/>\n'
            "</div>"
        )

        element = semantic_input(
            id="custom_label",
            value="world",
            semantic_label="hello",
            semantic_label_class="orange",
        )

        html = element.get_html_string()

        self.assertTrue(expected_html in html)


if __name__ == "__main__":
    unittest.main()
