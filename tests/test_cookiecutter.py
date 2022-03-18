import os
from subprocess import run, CompletedProcess
from pathlib import Path


def check_result(result: CompletedProcess, prev_cwd: Path):
    if result.stderr:
        os.chdir(prev_cwd)
        raise Exception(result.stderr.decode("utf-8"))
    if "ERROR:" in result.stdout.decode("utf-8"):
        os.chdir(prev_cwd)
        raise Exception(result.stdout.decode("utf-8"))
    if "FAILED" in result.stdout.decode("utf-8"):
        os.chdir(prev_cwd)
        raise Exception(result.stdout.decode("utf-8"))
    if "WARNING" in result.stdout.decode("utf-8"):
        os.chdir(prev_cwd)
        raise Exception(result.stdout.decode("utf-8"))


def test_bake_project(cookies, cookiecutter_dict):
    result = cookies.bake(extra_context=cookiecutter_dict)
    assert result.exit_code == 0
    assert result.exception is None


def test_pytest_in_baked_project(cookies, cookiecutter_dict):
    path = cookies.bake(extra_context=cookiecutter_dict).project_path
    prev_cwd = Path.cwd()
    os.chdir(path)
    result = run(
        "pip install --disable-pip-version-check -e .", shell=True, capture_output=True
    )
    check_result(result, prev_cwd)
    result = run("pytest tests", shell=True, capture_output=True)
    check_result(result, prev_cwd)
    os.chdir(prev_cwd)


def test_cli_in_baked_project(cookies, cookiecutter_dict):
    path = cookies.bake(extra_context=cookiecutter_dict).project_path
    prev_cwd = Path.cwd()
    os.chdir(path)
    result = run(
        "pip install --disable-pip-version-check -e .", shell=True, capture_output=True
    )
    check_result(result, prev_cwd)
    result = run(cookiecutter_dict["package_name"], shell=True, capture_output=True)
    check_result(result, prev_cwd)
    os.chdir(prev_cwd)


def test_pre_commit_in_baked_project(cookies, cookiecutter_dict):
    path = cookies.bake(extra_context=cookiecutter_dict).project_path
    prev_cwd = Path.cwd()
    os.chdir(path)
    result = run(
        "pip install --disable-pip-version-check pre-commit",
        shell=True,
        capture_output=True,
    )
    check_result(result, prev_cwd)
    result = run("git init --quiet && git add .", shell=True, capture_output=True)
    check_result(result, prev_cwd)
    result = run("pre-commit run --all-files", shell=True, capture_output=True)
    check_result(result, prev_cwd)
    os.chdir(prev_cwd)


def test_docs(cookies, cookiecutter_dict):
    path = cookies.bake(extra_context=cookiecutter_dict).project_path
    prev_cwd = Path.cwd()
    os.chdir(path)
    result = run(
        "pip install --disable-pip-version-check tox", shell=True, capture_output=True
    )
    check_result(result, prev_cwd)
    result = run("tox -e docs", shell=True, capture_output=True)
    check_result(result, prev_cwd)
    os.chdir(prev_cwd)


def test_lint(cookies, cookiecutter_dict):
    path = cookies.bake(extra_context=cookiecutter_dict).project_path
    prev_cwd = Path.cwd()
    os.chdir(path)
    result = run(
        "pip install --disable-pip-version-check tox", shell=True, capture_output=True
    )
    check_result(result, prev_cwd)
    result = run("git init --quiet && git add .", shell=True, capture_output=True)
    check_result(result, prev_cwd)
    result = run("tox -e lint", shell=True, capture_output=True)
    check_result(result, prev_cwd)
    os.chdir(prev_cwd)
