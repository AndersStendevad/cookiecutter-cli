from setuptools import setup

setup(
    name="{{cookiecutter.package_name}}",
    version="0.1.0",
    packages=["{{cookiecutter.package_name}}"],
    package_dir={"": "src"},
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            '{{cookiecutter.package_name}} = {{cookiecutter.package_name}}.cli:{{cookiecutter.package_name}}',
        ],
    },
)
