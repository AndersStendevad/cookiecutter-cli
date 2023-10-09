# cookiecutter-cli

My personal cookiecutter used to start a python project.

## Install for development

<code>pip install tox</code>
<code>pip install pre-commit</code>
<code>pre-commit install</code>

## Test the cookiecutter

<code>tox</code>

## Use the cookiecutter

<code>cookiecutter <PATH_TO_REPO / GIT_CLONE_LINK></code>

## Cruft

You can also use [Cruft](https://pypi.org/project/cruft/) to use the
cookiecutter. This enables you to make updates to your new project and fetch
the latest updates from this cookiecutter. I would recommend that you use cruft
to clone your projects instead of cookiecutter.

<code>cruft create <PATH_TO_REPO / GIT_CLONE_LINK></code>
