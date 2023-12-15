from dplib.actions.schema.check import check_schema


def test_check_schema():
    errors = check_schema("data/schema.json")
    assert len(errors) == 0


def test_check_schema_invalid():
    errors = check_schema("data/schema-invalid.json")
    assert len(errors) == 2
    error = errors[0]
    assert error.message == "'fields' is a required property"
    assert error.schema_path == "/required"
    assert error.object_path == "/"
    assert error.full_message == "[/] 'fields' is a required property"
