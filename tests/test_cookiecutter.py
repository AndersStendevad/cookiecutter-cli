import os
from subprocess import run, CompletedProcess
from pathlib import Path


def check_result(result: CompletedProcess, prev_cwd: Path):
    stderr = result.stderr.decode("utf-8")
    stdout = result.stdout.decode("utf-8")
    if result.stderr and "SetuptoolsDeprecationWarning" not in stderr:
        os.chdir(prev_cwd)
        raise Exception(stderr)
    if "ERROR:" in stdout:
        os.chdir(prev_cwd)
        raise Exception(stdout)
    if "FAILED" in stdout:
        os.chdir(prev_cwd)
        raise Exception(stdout)
    if "WARNING" in stdout:
        os.chdir(prev_cwd)
        raise Exception(stdout)


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
