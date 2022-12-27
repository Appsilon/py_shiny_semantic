import unittest

from htmltools import TagList

from shiny_semantic.elements import button, icon


class TestButton(unittest.TestCase):
    def test_semantic_button(self):
        test_case_1 = '<button id="test1" class="ui button">'
        test_case_2 = '<button id="test2" class="ui red basic button">'
        test_case_3 = '<i class="plane icon">'  # TODO: remove leading space when icon component is updated

        elements = TagList(
            button("test1", "Test1"),
            button("test2", "Test2", class_="red basic"),
            button("test3", "Test3", icon=icon("plane")),
        )

        html = elements.get_html_string()

        self.assertTrue(test_case_1 in html)
        self.assertTrue(test_case_2 in html)
        self.assertTrue(test_case_3 in html)


if __name__ == "__main__":
    unittest.main()
