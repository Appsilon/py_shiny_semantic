# This file ensures that COMPONENTS DEMO is deployed.
# Right now it is only possible to deploy one app at
# a time, so it's possible to switch to a different
# application later.

from shiny import App

from .components_demo.main import app_server, app_ui

app = App(app_ui, app_server)
