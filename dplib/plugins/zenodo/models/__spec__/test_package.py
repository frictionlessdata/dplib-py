from dplib.models import Package, Resource
from dplib.plugins.zenodo.models import ZenodoPackage


def test_zenodo_package():
    package = ZenodoPackage.from_path("data/plugins/zenodo/package.json")
    assert package.id == "5770714"
    assert len(package.pids) == 2
    assert package.pids["doi"].identifier == "10.5281/zenodo.5770714"
    assert package.created == "2021-12-10T05:47:07.709885+00:00"
    assert package.updated == "2021-12-14T09:04:24.503567+00:00"
    assert package.links["doi"] == "https://doi.org/10.5281/zenodo.5770714"
    assert package.metadata.title == "Fishway_Obstruction_Data_v1.csv"
    assert package.metadata.version == "v1"
    assert len(package.metadata.subjects) == 8
    assert package.metadata.subjects[0].subject == "fishways"
    assert len(package.metadata.creators) == 1
    assert len(package.files.entries) == 2
    resource = package.files.entries["Fishway_Obstruction_Data_v1.csv"]
    assert resource.key == "Fishway_Obstruction_Data_v1.csv"
    assert resource.size == 1377


def test_zenodo_package_to_dp():
    package = ZenodoPackage.from_path("data/plugins/zenodo/package.json").to_dp()
    assert package.id == "https://doi.org/10.5281/zenodo.5770714"
    assert package.title == "Fishway_Obstruction_Data_v1.csv"
    assert package.description
    assert package.description.startswith("<p>This dataset contains pool-weir")
    assert package.homepage == "https://zenodo.org/records/5770714"
    assert package.version == "v1"
    assert package.created == "2021-12-10T05:47:07.709885+00:00"
    assert len(package.contributors) == 1
    assert package.contributors[0].title == "Fuentes-Pérez, Juan Francisco"
    assert package.contributors[0].givenName == "Juan Francisco"
    assert package.contributors[0].familyName == "Fuentes-Pérez"
    assert package.contributors[0].roles == ["creator"]
    assert (
        package.contributors[0].organization
        == "Department of Hydraulics and Hydrology, ETSIIAA, University of Valladolid, 34004 Palencia, Spain"
    )
    assert package.keywords == [
        "fishways",
        "hydraulics",
        "smart fishways",
        "pool-weir",
        "hydrological variability",
        "nonuniformity",
        "clogging",
        "water-level sensors",
    ]
    assert len(package.resources) == 2
    assert package.resources[0].name == "fishway_obstruction_data_v1"
    assert (
        package.resources[0].path
        == "https://zenodo.org/records/5770714/files/Fishway_Obstruction_Data_v1.csv"
    )
    assert package.resources[0].format == "csv"
    assert package.resources[0].mediatype == "text/csv"
    assert package.resources[0].bytes == 1377
    assert package.resources[0].hash == "7bdef6756c84c3aea749f8211c557684"
    assert package.resources[1].name == "readme"
    assert (
        package.resources[1].path == "https://zenodo.org/records/5770714/files/readme.md"
    )
    assert package.resources[1].format == "md"
    assert package.resources[1].mediatype == "application/octet-stream"
    assert package.resources[1].bytes == 1577
    assert package.resources[1].hash == "a23a3c99befca45e706c9343e39f5926"


def test_zenodo_package_from_dp():
    package = ZenodoPackage.from_dp(Package.from_path("data/package-full.json"))
    assert package.metadata.title == "title"
    assert package.metadata.version == "1.0"
    assert package.metadata.description == "description"
    assert len(package.metadata.subjects) == 2
    assert package.metadata.subjects[0].subject == "keyword1"
    assert package.metadata.subjects[1].subject == "keyword2"
    assert package.files.entries["table.csv"].key == "table.csv"


def test_zenodo_package_from_dp_round_trip():
    package = ZenodoPackage.from_dp(
        ZenodoPackage.from_path("data/plugins/zenodo/package.json").to_dp()
    )
    assert package.metadata.title == "Fishway_Obstruction_Data_v1.csv"
    assert package.metadata.version == "v1"
    assert len(package.metadata.subjects) == 8
    assert package.metadata.subjects[0].subject == "fishways"
    assert len(package.files.entries) == 2
    resource = package.files.entries["Fishway_Obstruction_Data_v1.csv"]
    assert resource.key == "Fishway_Obstruction_Data_v1.csv"
    assert resource.size == 1377


def test_zenodo_package_from_dp_inline_resource():
    package = ZenodoPackage.from_dp(Package(resources=[Resource(data=[])]))
    assert package.to_dict() == {}
