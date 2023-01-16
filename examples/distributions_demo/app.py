# This app is treanslated from Posit's Shiny for Python examples
# Simulate data for a t-test
# https://shiny.rstudio.com/py/gallery/

from htmltools import div
from numpy import random
from shiny import App, reactive, render, ui

# Functions we import from stats.py
from stats import freqpoly, t_test

from shiny_semantic import page_semantic
from shiny_semantic.elements import header, segment, semantic_input, subheader
from shiny_semantic.modules import slider
from shiny_semantic.views import statistic


def card(title, *content):
    return div(
        {"class": "five wide column"},
        header(title, class_="small"),
        segment(
            *content,
            # TODO: this is not "semantic way" :D
            style=(
                "height:100%;"
                "margin:0;"
                "display:flex;"
                "gap: 0.6em;"
                "flex-direction:column;"
                "justify-content:space-around;"
            )
        ),
    )


app_ui = page_semantic(
    div(
        {"class": "ui center aligned padded stretched grid"},
        div(
            {"class": "fifteen wide column"},
            segment(
                header(
                    "Simulate data for a t-test",
                    subheader("with shiny-for-python and shiny-semantic"),
                    class_="big",
                ),
            ),
        ),
        card(
            "Distribution One",
            semantic_input(
                "n1",
                value=1000,
                min=1,
                type="number",
                semantic_label="n",
                class_="left labeled",
            ),
            semantic_input(
                "mean1",
                value=0,
                step=0.1,
                type="number",
                semantic_label="µ",
                class_="left labeled",
            ),
            semantic_input(
                "sd1",
                value=0.5,
                min=0.1,
                step=0.1,
                type="number",
                semantic_label="σ",
                class_="left labeled",
            ),
        ),
        card(
            "Distribution Two",
            semantic_input(
                "n2",
                value=1000,
                min=1,
                type="number",
                semantic_label="n",
                class_="left labeled",
            ),
            semantic_input(
                "mean2",
                value=0,
                step=0.1,
                type="number",
                semantic_label="µ",
                class_="left labeled",
            ),
            semantic_input(
                "sd2",
                value=0.5,
                min=0.1,
                step=0.1,
                type="number",
                semantic_label="σ",
                class_="left labeled",
            ),
        ),
        card(
            "Chart Configuration",
            semantic_input(
                "binwidth",
                value=0.1,
                step=0.1,
                type="number",
                semantic_label="Bin Width",
                class_="left labeled",
            ),
            div(
                header("Range", class_="tiny", style="text-align: initial;"),
                slider(
                    "range",
                    start_value=-3,
                    end_value=3,
                    min_value=-5,
                    max_value=5,
                ),
            ),
        ),
        div(
            {"class": "ten wide column"},
            segment(ui.output_plot("hist")),
        ),
        div(
            {"class": "five wide column"},
            segment(
                statistic(
                    ui.output_text("t_value"),
                    "t-value",
                    value_first=False,
                ),
                statistic(
                    ui.output_text("dof"),
                    "Degrees of Freedom",
                    value_first=False,
                ),
                statistic(
                    ui.output_text("p_value"),
                    "p-value",
                    value_first=False,
                ),
                style_=(
                    "display: flex;" "flex-direction: column;" "justify-content: space-evenly;"
                ),
            ),
        ),
    )
)


def server(input, output, session):
    @reactive.Calc
    def generated_data():
        distribution_one = random.normal(input.mean1(), input.sd1(), input.n1())
        distrbution_two = random.normal(input.mean2(), input.sd2(), input.n2())
        return {"d1": distribution_one, "d2": distrbution_two}

    @reactive.Calc
    def test_result():
        return t_test(generated_data()["d1"], generated_data()["d2"])

    @output(id="hist")
    @render.plot
    def _():
        return freqpoly(
            generated_data()["d1"],
            generated_data()["d2"],
            input.binwidth(),
            input.range(),
        )

    @output(id="t_value")
    @render.text
    def _():
        return round(test_result()["t"], 3)

    @output(id="dof")
    @render.text
    def _():
        return round(test_result()["dof"], 1)

    @output(id="p_value")
    @render.text
    def _():
        return round(test_result()["p"], 3)


app = App(app_ui, server)
