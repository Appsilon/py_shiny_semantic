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

## How to install

`shiny_semantic` is available from the official [PyPI distribution](https://pypi.org/project/shiny-semantic), and can be installed using pip. Please remember, that it is considered to be best practice to install packages in isolated virtual environments (see the next section).

```
pip install shiny_semantic
```

This will install both `shiny` and `shiny_semantic` - it is enough to start creating a Shiny application in Python.

## Development

In this project we used only those python tools that already come with a standard python distribution and should be immediately available to the developers. For package management we used `pip`, for virtual environment we used `venv`, and for unit tests we used `unittest`.

Please note, that some systems (e.g. macOS) have Python installed by default, and it may be accessible with `python3` rather than just `python`. As soon as you init and source a venv, you will be able to call python with just `python`.

To start development, run the following command:

```shell
python -m venv .venv # creates virtual environment
source .venv/bin/activate # activates virtual environment
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

# It is best to remove local dist folder, so that `twine` is not confused on which version to use
rm -rf dist

python -m build
twine check dist/*

# Currently, the package is published by pavel.demin@appsilon.com
twine upload dist/*
```

## How to update the Fomantic components

The easiest way to replace the Fomantic assets with the new ones, is as follows:

1. Navigate to https://www.jsdelivr.com/package/npm/fomantic-ui. This resource is recommended by the Fomantic team - it contains the latest version of the library files
2. Download the entire folder as a _.tgz_ archive
3. Unpack the archive
4. Find _dist_ folder, grab the minimized versions of CSS and JS files and move them into _shiny_semantic/www/semantic/_
5. In the same _dist_ folder, locate the _themes_ subfolder - open it
6. Move the _default_ folder into _shiny_semantic/www/semantic/themes_ - this way Fomantic JS and CSS will be able to seamlessly pick up fonts and icons.
