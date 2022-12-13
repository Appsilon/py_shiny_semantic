# py_shiny_semantic

Python implementation of Appsilon's `shiny.semantic`

## Development

```shell
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

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
