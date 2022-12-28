import unittest

from shiny_semantic.modules import slider


class TestSlider(unittest.TestCase):
    def test_simple_slider(self):
        expected_html = (
            '<div id="simple" class="ui labeled slider ss-slider" '
            + 'data-min="0" data-max="5" data-start="0" data-labels="null">'
            + "</div>"
        )

        element = slider(
            id="simple",
            label="simple",
            min_value=0,
            max_value=5,
            start_value=0,
        )

        html = element.get_html_string()

        self.assertTrue(expected_html in html)

    def test_range_slider(self):
        expected_html = (
            '<div id="range" class="ui labeled range slider ss-slider" '
            + 'data-min="0" data-max="5" data-start="0" data-end="2" data-labels="null">'
            + "</div>"
        )

        element = slider(
            id="range",
            label="range",
            min_value=0,
            max_value=5,
            start_value=0,
            end_value=2,
        )

        html = element.get_html_string()

        self.assertTrue(expected_html in html)

    def test_custom_slider(self):
        expected_html = (
            '<div id="slider_custom" class="ui big red labeled slider ss-slider" '
            + 'data-min="1" data-max="5" data-start="3" data-step="1" '
            + 'data-labels="[&quot;A&quot;, &quot;B&quot;, &quot;C&quot;, &quot;D&quot;, &quot;E&quot;, &quot;F&quot;]">'
            + "</div>"
        )

        element = slider(
            id="slider_custom",
            label="Custom Slider",
            min_value=1,
            max_value=5,
            start_value=3,
            step=1,
            show_ticks=False,
            show_labels=True,
            custom_labels=["A", "B", "C", "D", "E", "F"],
            class_="big red",
        )

        html = element.get_html_string()

        self.assertTrue(expected_html in html)


if __name__ == "__main__":
    unittest.main()
