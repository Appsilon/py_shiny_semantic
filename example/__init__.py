from shiny import App

from .main import app_server, app_ui

app = App(app_ui, app_server)
