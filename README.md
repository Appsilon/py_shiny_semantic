# Semantic UI in Shiny-for-Python

[![stability-alpha](https://img.shields.io/badge/stability-alpha-f4d03f.svg)](https://github.com/mkenney/software-guides/blob/master/STABILITY-BADGES.md#alpha)

_Create rich web applications in PyShiny using styles and components from Semantic UI._

## About the project

This is an early [Shiny-for-Python](https://shiny.rstudio.com/py/) implementation of [the official community fork of Semantic UI](https://fomantic-ui.com/).

The repository contains a python package `shiny_semantic` and a PyShiny application (found in `example` folder) that serves as a simple demo of the implemented components.

The application is deployed on RSConnect and can be found at https://connect.appsilon.com/py_shiny_semantic/.

## About Fomantic UI

[Fomantic UI](https://fomantic-ui.com/) is a well-maintained community fork of a more widely known and mature [Semantic UI](https://semantic-ui.com/). This project uses JS, CSS and icons from Fomantic UI while referring to the name of the original library.

The structure of `shiny_semantic` follows the one of Fomantic UI -- this way users may easily refer to corresponding sections in the original documentation to learn about possible classes, styles and behaviors of the components.

## Repository structure

- _.github_
  - Github workflows to run CI using Github Actions.
- _.vscode_
  - Visual Studio Code specific settings and recommended extensions. Useful to ensure standardized code style in a dev team.
- _example_
  - Shiny application that is split into many shiny-modules, where each module represents one feature/component. This folder serves as an entry point for the Shiny app to run.
- _shiny_semantic_
  - Python package that implements the Fomantic components. The package's structure is similar to the underlying Fomantic library: all components are split into elements, collections, views and modules.
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
python -m venv .venv # creates virtual environment
source .venv/bin/activate # activates virtual environment
pip install shiny==0.2.9 # TODO: remove when shiny_semantic is published to PyPI
pip install -e ".[dev]
```

This project uses [pre-commit](https://pre-commit.com/) to ensure the quality of code style. Once the dependencies are restored, run the following command once:

```shell
pre-commit install
```

To run the app in the hot-reload mode (the app automatically reloads every time it detects changes in the python source code), run the following command:

```
shiny run --reload example
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
    --entrypoint example \
    --exclude "**/*.pyc" \
    --exclude .DS_Store \
    --exclude dist \
    --exclude "*.egg-info" \
    --exclude tests \
    . # DIRECTORY
```

When developing a feature on a feature branch, you can make a manual deployment (it is recommended to delete such deployments after the feature is merged into main):

```
rsconnect deploy shiny --entrypoint example .
```

## How to update the package

This project leverages [bumpver](https://github.com/mbarkhau/bumpver) to handle package versioning. To make sure that `bumpver` works, run the following commands:

```shell
pip install bumpver
bumpver update --patch --dry --no-fetch
```

This should provide the developer with a preview of changed lines across multiple files - where package version is mentioned. When local updates are fininshed, the developer might run:

```shell
bumpver update --patch # or --minor or --major, depending on the PR goal
```

This command will change the abovementioned string versions, create a commit with "bump version" message, create a git tag and will push changes to the remote. Developers will find a new version under "Releases" section on the Github page.

## How to build and publish the package

```shell
pip install build twine
python -m build
twine check dist/*

# Currently, the package is publihsed by pavel.demin@appsilon.com
# TODO: replace testpypi with the real pypi when the package is published
twine upload -r testpypi dist/*
```

## How to update the Fomantic components

The easiest way to replace the Fomantic assets with the new ones, is as follows:

1. Navigate to https://www.jsdelivr.com/package/npm/fomantic-ui. This resource is recommended by the Fomantic team - it contains the latest version of the library files
2. Download the entire folder as a _.tgz_ archive
3. Unpack the archive
4. Find _dist_ folder, grab the minimized versions of CSS and JS files and move them into _shiny_semantic/www/semantic/_
5. In the same _dist_ folder, locate the _themes_ subfolder - open it
6. Move the _default_ folder into _shiny_semantic/www/semantic/themes_ - this way Fomantic JS and CSS will be able to seamlessly pick up fonts and icons.
