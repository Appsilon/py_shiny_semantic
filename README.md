# Shiny Semantic for Python

This packages makes Fomantic UI available to Shiny developers in Python. Fomantic UI is a well-maintained community fork of the famous Semantic UI, hence the name of this package.

## Development

```shell
# Init a virtual environmet that will host all python dependencies for this project
# We use venv as it is part of the standard library
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Run the app with hot reload (app reloads when changes are detected)
shiny run --reload app.py
```

## Deployment

```shell
# Install rsconnect CLI
pip install rsconnect-python

# First-time configuration (replace with your API key)
rsconnect add -n connect.appsilon.com -s https://connect.appsilon.com/ -k $RSCONNECT_API

# Manual deployment
rsconnect deploy shiny .

# Write manifest for git-backed deployment
rsconnect write-manifest shiny .
```
