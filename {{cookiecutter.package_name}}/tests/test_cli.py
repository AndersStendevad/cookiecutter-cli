from {{cookiecutter.package_name}}.cli import {{cookiecutter.package_name}}


def test_{{cookiecutter.package_name}}(runner):
    with runner.isolated_filesystem():
        result = runner.invoke({{cookiecutter.package_name}}, ["world"])
        assert not result.exception
        assert result.output == 'Hello world!\n'
