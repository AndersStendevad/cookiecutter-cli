from {{cookiecutter.package_name}} import __version__ as VERSION
from {{cookiecutter.package_name}}.cli import {{cookiecutter.package_name}}


def test_{{cookiecutter.package_name}}(runner):
    with runner.isolated_filesystem():
        result = runner.invoke({{cookiecutter.package_name}}, ["--version"])
        assert not result.exception
        assert result.output == f"{VERSION}\n"
