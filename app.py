from shiny import App, ui

from shiny_semantic import page_semantic

app_ui = page_semantic(
    ui.tags.div(
        ui.tags.div(
            ui.tags.h1(
                "Shiny Semantic: Components Demo",
                class_="ui inverted header",
                style="margin-block: 5em;",
            ),
            class_="ui text container",
        ),
        class_="ui inverted vertical masthead center aligned segment",
    ),
)


def app_server(input, output, session):
    pass


app = App(app_ui, app_server)
