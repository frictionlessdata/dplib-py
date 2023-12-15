from dplib.actions.resource.check import check_resource
from dplib.models import Resource


def test_check_resource():
    errors = check_resource("data/resource.json")
    assert len(errors) == 0


def test_check_resource_invalid():
    errors = check_resource("data/resource-invalid.json")
    assert len(errors) == 1
    error = errors[0]
    assert error.message == "1 is not of type 'string'"
    assert error.schema_path == "/properties/name/type"
    assert error.object_path == "/name"
    assert error.full_message == "[/name] 1 is not of type 'string'"


def test_check_resource_invalid_dereferencing():
    errors = check_resource("data/resource-invalid-dereferencing.json")
    assert len(errors) == 1
    error = errors[0]
    assert error.full_message == "[/dialect/delimiter] 1 is not of type 'string'"


def test_check_resource_from_model():
    resource = Resource(name="name", path="path")
    errors = check_resource(resource)
    assert len(errors) == 0
