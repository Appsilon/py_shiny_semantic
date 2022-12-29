import unittest

from htmltools import TagList

from shiny_semantic.modules import checkbox, checkbox_group


class TestCheckbox(unittest.TestCase):
    def test_single_checkbox(self):
        expected_html_1 = (
            '<div id="test1" class="ui checkbox">\n'
            '  <input id="test1" type="checkbox" name="test1"/>\n'
            '  <label for="test1">Test1</label>\n'
            "</div>"
        )
        expected_html_2 = (
            '<div id="test2" class="ui checked radio checkbox">\n'
            '  <input id="test2" type="radio" name="test2" checked=""/>\n'
            '  <label for="test2">Test2</label>\n'
            "</div>"
        )
        expected_html_3 = (
            '<div id="test3" class="ui slider checkbox">\n'
            '  <input id="test3" type="checkbox" name="test3"/>\n'
            '  <label for="test3">Test3</label>\n'
            "</div>"
        )
        expected_html_4 = (
            '<div id="test4" class="ui toggle checkbox">\n'
            '  <input id="test4" type="checkbox" name="test4"/>\n'
            '  <label for="test4">Test4</label>\n'
            "</div>"
        )

        elements = TagList(
            checkbox("test1", "Test1"),
            checkbox("test2", "Test2", value=True, type="radio"),
            checkbox("test3", "Test3", type="slider"),
            checkbox("test4", "Test4", type="toggle"),
        )

        html = elements.get_html_string()

        self.assertTrue(expected_html_1 in html)
        self.assertTrue(expected_html_2 in html)
        self.assertTrue(expected_html_3 in html)
        self.assertTrue(expected_html_4 in html)


if __name__ == "__main__":
    unittest.main()
