# Fomantic UI components in Shiny-for-Python

## About the project

The project was a three weeks long attempt/research on how to implement [Fomantic UI](https://fomantic-ui.com/) in [Shiny-for-Python](https://shiny.rstudio.com/py/).

The result of this project consists of two units: `shiny_semantic` Python package and PyShiny application, that serves as a simple demo of the implemented components.

The application is deployed on RSConnect and can be found at https://connect.appsilon.com/py_shiny_semantic/.

## Repository structure

- _.github_
  - Github workflows to run CI using Github Actions.
- _.vscode_
  - Visual Studio Code specific settings and recommended extensions. Useful to ensure standardized code style in a dev team.
- _app_
  - Shiny application that is split into many shiny-modules, where each module represents one feature/component. This folder serves as an entrypoint for the Shiny app to run.
- _shiny_semantic_
  - Python package that implements the Fomantic components. The package;s structure is similar to the underlying Fomantic library: all components are split into elements, collections, views and modules.
  - Folders that are not from Fomantic are _tests_ for unit tests, _types_ for custom Python typings and _www_ for Shiny bindings (JS code) as well as static assets (Fomantic fonts, CSS and JS code).
- _root-level files_
  - _manifest.json_ - created with `rsconnect` to enable git-backed deployment
  - _requirements.txt_ - generated with `pip freeze`, contains all project's dependencies along with their versions
  - _README.md_ - this documentation file.

## Development

In this project we used only those python tools that already come with a standard python distribution and should be immediately available to the developers. For package management we used `pip`, for virtual environment we used `venv`, and for unit tests we used `unittest`.

Please note, that some systems (e.g. macOS) have Python installed by default, and it may be accessible with `python3` rather than just `python`. As soon as you init and source a venv, you will be able to call python with just `python`.

To start development, run the following command:

```shell
python -m venv venv # creates virtual environment
source venv/bin/activate # activates virtual environment
pip install -r requirements.txt # installs dependencies
```

To run the app in the hot-reload mode (the app automatically reloads evey time it detects changes in the python source code), run the following command:

```
shiny run --reload app
```

## Deployment

Shiny-for-Python allows easy deployment on RSConnect. First, make sure that the rsconnect CLI client is installed:

```shell
pip install rsconnect-python
```

First time configuration for the Appsilon team:

```
rsconnect add \
    --name connect.appsilon.com \
    --server https://connect.appsilon.com/ \
    --key <Insert your API key>
```

This repository has a configured CD via git-backed deployment on RSConnect thanks to the _manifest.json_ file that can be found at the root level of this project. To generate this file, use the following command:

```
rsconnect write-manifest shiny \
    --overwrite \
    --entrypoint app \
    --exclude "**/*.pyc" \
    --exclude .DS_Store \
    . # DIRECTORY
```

When developing a feature on a feature branch, you can make a manual deployment (it is recommended to delete suche deployments after the feature is merged into main):

```
rsconnect deploy shiny --entrypoint app .
```

## How to update the Fomantic

The easiest way to replace the Fomantic assets with the new ones, is as follows:

1. Navigate to https://www.jsdelivr.com/package/npm/fomantic-ui. This resource is recommended by the Fomantic team - it contains the lates version of the library files
2. Download the entire folder as a _.tgz_ archive
3. Unpack the archive
4. Find _dist_ folder, grab the minimized versions of CSS and JS files and move them into _shiny_semantic/www/semantic/_
5. In the same _dist_ folder, locate the _themes_ subfolder - open it
6. Move the _default_ folder into _shiny_semantic/www/semantic/themes_ - this way Fomantic JS and CSS will be able to seamlessly pick up fonts and icons.
