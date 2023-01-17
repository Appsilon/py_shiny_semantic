# This file ensures that COMPONENTS DEMO is deployed.
# Right now it is only possible to deploy one app at
# a time, so it's possible to switch to a different
# application later.

# It is also not possible to create separate manifest.json
# inside each application to deploy them separately, since
# they will fail to install shiny_semantic until it is published.

from shiny import App

from .distributions_demo.main import app_server, app_ui

app = App(app_ui, app_server)
