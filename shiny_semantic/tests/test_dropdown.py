import unittest

from shiny_semantic.modules import dropdown, input_select


class TestDropdown(unittest.TestCase):
    def test_dropdown(self):
        expected_html_1 = '<div id="dropdown" class="ui selection dropdown semantic-select-input" data-settings="null">'  # noqa: E501
        expected_html_2 = '<input type="hidden" name="dropdown"/>'
        expected_html_3 = '<div class="default text"></div>'
        expected_html_4 = '<div class="item" data-value="0">0</div>'

        element = dropdown("dropdown", [str(x) for x in range(5)])

        html = element.get_html_string()

        self.assertTrue(expected_html_1 in html)
        self.assertTrue(expected_html_2 in html)
        self.assertTrue(expected_html_3 in html)
        self.assertTrue(expected_html_4 in html)

    def test_input_select(self):
        expected_html_1 = '<div class="ui form">'
        expected_html_2 = '<div class="field">'
        expected_html_3 = 'data-settings="{&quot;clearable&quot;: true}'
        expected_html_4 = '<div class="default text">Select</div>'

        element = input_select(
            id="select",
            label="Select",
            choices=[str(x) for x in range(5)],
            placeholder="Select",
            settings={"clearable": True},
        )

        html = element.get_html_string()

        self.assertTrue(expected_html_1 in html)
        self.assertTrue(expected_html_2 in html)
        self.assertTrue(expected_html_3 in html)
        self.assertTrue(expected_html_4 in html)


if __name__ == "__main__":
    unittest.main()
