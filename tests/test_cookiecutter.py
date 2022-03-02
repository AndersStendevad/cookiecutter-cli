import os
import subprocess
from pathlib import Path

def test_bake_project(cookies, cookiecutter_dict):
    result = cookies.bake(extra_context=cookiecutter_dict)

    assert result.exit_code == 0
    assert result.exception is None

def test_tox_in_baked_project(cookies, cookiecutter_dict):
    path = cookies.bake(extra_context=cookiecutter_dict).project_path
    prev_cwd = Path.cwd()
    os.chdir(path)
    result = subprocess.run("pip3 install -e .", shell=True, capture_output=True)
    if result.stderr:
        raise Exception(result.stderr.decode('utf-8'))
    result = subprocess.run("pytest", shell=True, capture_output=True)
    if result.stderr:
        raise Exception(result.stderr.decode('utf-8'))
    os.chdir(prev_cwd)
