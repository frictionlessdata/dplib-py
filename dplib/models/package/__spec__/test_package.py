import pytest
from pydantic import ValidationError

from dplib import settings
from dplib.models import Dialect, Package, Resource, Schema


def test_package_from_path():
    package = Package.from_path("data/package.json")
    assert package.name == "name"
    assert len(package.resources) == 1
    assert package.resources[0].name == "name"
    assert package.resources[0].path == "table.csv"


def test_package_from_path_full():
    package = Package.from_path("data/package-full.json")
    assert package.name == "name"
    assert package.title == "title"
    assert package.description == "description"
    assert package.version == "1.0"
    assert package.homepage == "http://example.com"
    assert package.licenses[0].path == "path"
    assert package.sources[0].path == "path"
    assert package.contributors[0].path == "path"
    assert package.keywords[0] == "keyword1"
    assert package.image == "http://example.com/image.png"
    assert package.created == "2017-01-01T00:00:00Z"


def test_package_from_text():
    text = '{"name": "name"}'
    package = Package.from_text(text, format="json")
    assert package.name == "name"


def test_package_from_dict():
    data = {"name": "name"}
    package = Package.from_dict(data)
    assert package.name == "name"


def test_package_from_dict_invalid():
    data = {"name": 1}
    with pytest.raises(ValidationError):
        Package.from_dict(data)


def test_package_set_proprty_invalid():
    package = Package()
    with pytest.raises(ValidationError):
        package.name = 1  # type: ignore


def test_package_get_resource_by_name():
    package = Package.from_path("data/package.json")
    resource = package.get_resource(name="name")
    assert resource
    assert resource.name == "name"
    assert resource.path == "table.csv"


def test_package_get_resource_by_path():
    package = Package.from_path("data/package.json")
    resource = package.get_resource(path="table.csv")
    assert resource
    assert resource.name == "name"
    assert resource.path == "table.csv"


def test_package_resources_basepath():
    package = Package.from_path("data/package.json")
    resource = package.get_resource(name="name")
    assert resource
    assert resource.basepath == "data"


def test_package_add_resource():
    package = Package()
    package.add_resource(Resource(name="name", path="table.csv"))
    resource = package.get_resource(name="name")
    assert resource
    assert resource.name == "name"
    assert resource.path == "table.csv"


def test_package_add_resource_with_basepath():
    package = Package(basepath="data")
    package.add_resource(Resource(name="name", path="table.csv"))
    resource = package.get_resource(name="name")
    assert resource
    assert resource.name == "name"
    assert resource.path == "table.csv"
    assert resource.basepath == "data"


def test_package_dereference():
    package = Package.from_path("data/package-full.json")
    package.dereference()
    resource = package.get_resource(name="name")
    assert resource
    assert isinstance(resource.dialect, Dialect)
    assert resource.dialect.delimiter == ";"
    assert isinstance(resource.schema, Schema)
    assert len(resource.schema.fields) == 2


def test_package_contributors_role_v1():
    package = Package.from_dict({"contributors": [{"role": "author"}]})
    assert package.contributors[0].custom == {}
    assert package.contributors[0].roles == ["author"]


def test_package_to_dict():
    package = Package()
    assert package.to_dict() == {
        "$schema": settings.PROFILE_CURRENT_PACKAGE,
    }
    package.add_resource(Resource(name="name"))
    assert package.to_dict() == {
        "$schema": settings.PROFILE_CURRENT_PACKAGE,
        "resources": [{"name": "name"}],
    }
    package.profile = settings.PROFILE_DEFAULT_PACKAGE
    assert package.to_dict() == {
        "$schema": settings.PROFILE_DEFAULT_PACKAGE,
        "resources": [{"name": "name"}],
    }
