"""{{cookiecutter.package_name}} CLI"""

import click


@click.command()
@click.argument("name", default="world")
def {{cookiecutter.package_name}}(name):
    """Hello World"""
    click.echo(f"Hello {name}!")


if __name__ == "__main__":
    {{cookiecutter.package_name}}()
