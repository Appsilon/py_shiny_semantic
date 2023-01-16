# This app is treanslated from Posit's Shiny for Python examples
# Simulate data for a t-test
# https://shiny.rstudio.com/py/gallery/

from htmltools import div
from numpy import random
from shiny import App, render, ui

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
            semantic_input("n1", label="n", value=1000, min=1, type="number"),
            semantic_input("mean1", label="µ", value=0, step=0.1, type="number"),
            semantic_input("sd1", label="σ", value=0.5, min=0.1, step=0.1, type="number"),
        ),
        card(
            "Distribution Two",
            semantic_input("n2", label="n", value=1000, min=1, type="number"),
            semantic_input("mean2", label="µ", value=0, step=0.1, type="number"),
            semantic_input("sd2", label="σ", value=0.5, min=0.1, step=0.1, type="number"),
        ),
        card(
            "Chart Configuration",
            semantic_input("binwidth", label="Bin width", value=0.1, step=0.1, type="number"),
            slider(
                "range",
                start_value=-3,
                end_value=3,
                min_value=-5,
                max_value=5,
            ),
        ),
        div(
            {"class": "ten wide column"},
            segment(ui.output_plot("hist")),
        ),
        div(
            {"class": "five wide column"},
            segment(
                statistic(0.29, "t-value", value_first=False),
                statistic(197.17, "Degrees of Freedom", value_first=False),
                statistic(0.30, "p-value", value_first=False),
                style_=(
                    "display: flex;" "flex-direction: column;" "justify-content: space-evenly;"
                ),
            ),
        ),
    )
)


def server(input, output, session):
    @output
    @render.plot
    def hist():
        x1 = random.normal(input.mean1(), input.sd1(), input.n1())
        x2 = random.normal(input.mean2(), input.sd2(), input.n2())
        return freqpoly(x1, x2, input.binwidth(), input.range())

    @output
    @render.text
    def ttest():
        x1 = random.normal(0, 1, 100)
        x2 = random.normal(0, 1, 100)
        return t_test(x1, x2)


app = App(app_ui, server)
