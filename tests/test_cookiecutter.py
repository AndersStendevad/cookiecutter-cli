def test_bake_project(cookies, cookiecutter_dict):
    result = cookies.bake(extra_context=cookiecutter_dict)

    assert result.exit_code == 0
