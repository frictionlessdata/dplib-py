from dplib.models import Package, Resource
from dplib.plugins.ckan.models import CkanPackage


def test_ckan_package():
    package = CkanPackage.from_path("data/plugins/ckan/package.json")
    assert package.name == "sample-dataset-1"
    assert package.title == "Sample Dataset"
    assert package.organization
    assert package.organization.name == "sample-organization"
    assert package.version == "1.0"
    assert package.license_id == "cc-by"
    assert len(package.resources) == 9
    assert len(package.tags) == 8
    assert package.resources[0].name == "sample-linked.csv"
    assert package.tags[0].name == "csv"


def test_ckan_package_to_dp():
    package = CkanPackage.from_path("data/plugins/ckan/package.json").to_dp()
    assert package.name == "sample-dataset-1"
    assert package.title == "Sample Dataset"
    assert package.version == "1.0"
    assert package.licenses[0].name == "cc-by"
    assert len(package.resources) == 9
    assert len(package.keywords) == 8
    assert len(package.contributors) == 2
    assert (
        package.resources[0].path
        == "https://raw.githubusercontent.com/datopian/CKAN_Demo_Datasets/main/resources/org1_sample.csv"
    )
    assert package.keywords[0] == "csv"
    assert package.contributors[0].title == "Test Author"
    assert package.contributors[0].roles == ["author"]
    assert package.custom["ckan:id"] == "c322307a-b871-44fe-a602-32ee8437ff04"


def test_ckan_package_from_dp():
    package = CkanPackage.from_dp(Package.from_path("data/package-full.json"))
    assert package.name == "name"
    assert package.name == "name"
    assert package.title == "title"
    assert package.notes == "description"
    assert package.version == "1.0"
    assert package.license_id == "name"
    assert package.license_title == "title"
    assert package.license_url == "path"
    assert len(package.resources) == 1
    assert package.resources[0].name == "table.csv"
    assert len(package.tags) == 2
    assert package.tags[0].name == "keyword1"
    assert package.tags[1].name == "keyword2"


def test_ckan_package_from_dp_round_trip():
    package = CkanPackage.from_dp(
        CkanPackage.from_path("data/plugins/ckan/package.json").to_dp()
    )
    assert package.name == "sample-dataset-1"
    assert package.title == "Sample Dataset"
    assert package.version == "1.0"
    assert package.license_id == "cc-by"
    assert len(package.resources) == 9
    assert len(package.tags) == 8
    assert package.resources[0].name == "org1_sample.csv"
    assert package.tags[0].name == "csv"


def test_ckan_package_from_dp_inline_resource():
    package = CkanPackage.from_dp(Package(resources=[Resource(data=[])]))
    assert package.to_dict() == {}
