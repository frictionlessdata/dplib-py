from dplib.actions.dialect.check import check_dialect


def test_check_dialect():
    errors = check_dialect("data/dialect.json")
    assert len(errors) == 0


def test_check_dialect_invalid():
    errors = check_dialect("data/dialect-invalid.json")
    assert len(errors) == 1
    error = errors[0]
    assert error.message == "1 is not of type 'string'"
    assert error.schema_path == "/properties/delimiter/type"
    assert error.object_path == "/delimiter"
    assert error.full_message == "[/delimiter] 1 is not of type 'string'"
