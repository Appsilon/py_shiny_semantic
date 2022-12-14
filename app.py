from shiny import App, ui

app_ui = ui.tags.div("Hello World")


def app_server(input, output, session):
    pass


app = App(app_ui, app_server)
