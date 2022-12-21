import unittest

from shiny import App

from shiny_semantic import page_semantic
from shiny_semantic.elements import button


class TestButton(unittest.TestCase):
    def test_semantic_button(self):
        test_case_1 = '<button id="test1" class="ui  button">'
        test_case_2 = '<button id="test2" class="ui red basic button">'
        test_case_3 = '<i class="plane icon">'

        app = App(
            ui=page_semantic(
                button("test1", "Test1"),
                button("test2", "Test2", class_name="red basic"),
                button("test3", "Test3", icon_name="plane"),
            ),
            server=None,
        )

        html = app.ui.get("html")

        self.assertTrue(test_case_1 in html)
        self.assertTrue(test_case_2 in html)
        self.assertTrue(test_case_3 in html)


if __name__ == "__main__":
    unittest.main()