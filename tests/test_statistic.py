import unittest

from htmltools import TagList

from shiny_semantic.elements import icon
from shiny_semantic.views import statistic


class TestIcon(unittest.TestCase):
    def test_icon(self):
        expected_html_1 = (
            '<div class="ui statistic">\n'
            '  <div class="value">12</div>\n'
            '  <div class="label">users</div>\n'
            "</div>"
        )
        expected_html_2 = (
            '<div class="ui statistic">\n'
            '  <div class="label">world</div>\n'
            '  <div class="value">hello</div>\n'
            "</div>"
        )
        expected_html_3 = (
            '<div class="ui red statistic">\n'
            '  <div class="value">\n'
            '    <i class="person icon"></i>\n'
            "    people\n"
            "  </div>\n"
            '  <div class="label">available</div>\n'
            "</div>"
        )

        elements = TagList(
            statistic(12, "users"),
            statistic("hello", "world", value_first=False),
            statistic(
                TagList(icon("person"), "people"),
                "available",
                class_="red",
            ),
        )

        html = elements.get_html_string()

        self.assertTrue(expected_html_1 in html)
        self.assertTrue(expected_html_2 in html)
        self.assertTrue(expected_html_3 in html)


if __name__ == "__main__":
    unittest.main()
