import pytest

from dplib.actions.package.check import check_package
from dplib.models import Package

# TODO: move to corresponding action folder
# For some reason pytest colelction failed if we used folders in Python3.11/12


def test_check_package():
    errors = check_package("data/package.json")
    assert len(errors) == 0


def test_check_package_invalid():
    errors = check_package("data/package-invalid.json")
    assert len(errors) == 1
    error = errors[0]
    assert error.message == "1 is not of type 'string'"
    assert error.schema_path == "/properties/name/type"
    assert error.object_path == "/name"
    assert error.full_message == "[/name] 1 is not of type 'string'"


def test_check_package_invalid_dereferencing():
    errors = check_package("data/package-invalid-dereferencing.json")
    assert len(errors) == 1
    error = errors[0]
    # TODO: extend error path so it shows the full path from the package root
    assert error.full_message == "[/delimiter] 1 is not of type 'string'"


@pytest.mark.vcr
def test_check_package_custom_profile():
    errors = check_package("data/package-custom-profile.json")
    assert len(errors) == 1
    error = errors[0]
    assert error.full_message == "[/] 'requiredProperty' is a required property"


def test_check_package_from_model():
    package = Package(name="name")
    errors = check_package(package)
    assert len(errors) == 1
