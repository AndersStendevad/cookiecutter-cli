import pytest
import json


@pytest.fixture
def cookiecutter_dict():
    with open("cookiecutter.json") as file:
        return json.load(file)
