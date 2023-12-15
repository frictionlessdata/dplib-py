from dplib.models import Package
from dplib.plugins.dcat.models import DcatPackage


def test_dcat_package():
    package = DcatPackage.from_path("data/plugins/dcat/package.xml")
    assert package.title == "Fishway_Obstruction_Data_v1.csv"
    assert package.version == "v1"
    assert package.description
    assert package.description.startswith("This dataset contains pool-weir type fishway")
    assert package.issued == "2021"
    assert package.is_version_of == ["https://doi.org/10.5281/zenodo.5770713"]
    assert package.identifier == "https://doi.org/10.5281/zenodo.5770714"
    assert package.languages == [
        "http://publications.europa.eu/resource/authority/language/ENG"
    ]
    assert package.pages == ["https://doi.org/10.5281/zenodo.5770714"]
    assert len(package.keywords) == 8
    assert package.keywords[0] == "fishways"
    assert len(package.distributions) == 3
    assert (
        package.distributions[1].download_url
        == "https://zenodo.org/records/5770714/files/Fishway_Obstruction_Data_v1.csv"
    )
    assert package.distributions[1].byte_size == 1377
    assert package.distributions[1].media_type == "text/csv"


def test_dcat_package_to_dp():
    package = DcatPackage.from_path("data/plugins/dcat/package.xml").to_dp()
    assert package.id == "https://doi.org/10.5281/zenodo.5770714"
    assert package.resources[1].bytes == 1577
    assert package.title == "Fishway_Obstruction_Data_v1.csv"
    assert package.description
    assert package.description.startswith("This dataset contains pool-weir type fishway")
    assert package.version == "v1"
    assert len(package.keywords) == 8
    assert package.keywords[0] == "fishways"
    assert len(package.resources) == 2
    assert package.resources[0].name == "fishway_obstruction_data_v1"
    assert (
        package.resources[0].path
        == "https://zenodo.org/records/5770714/files/Fishway_Obstruction_Data_v1.csv"
    )
    assert package.resources[0].mediatype == "text/csv"
    assert package.resources[0].bytes == 1377
    assert package.resources[1].name == "readme"
    assert (
        package.resources[1].path == "https://zenodo.org/records/5770714/files/readme.md"
    )


def test_dcat_package_from_dp():
    package = DcatPackage.from_dp(Package.from_path("data/package-full.json"))
    assert package.identifier == "id"
    assert len(package.distributions) == 1
    assert package.distributions[0].download_url == "table.csv"
    assert package.description == "description"
    assert package.homepage == "http://example.com"
    assert package.issued == "2017-01-01T00:00:00Z"
    assert package.keywords == ["keyword1", "keyword2"]
    assert package.title == "title"
    assert package.version == "1.0"


def test_dcat_package_from_dp_round_trip():
    package = DcatPackage.from_dp(
        DcatPackage.from_path("data/plugins/dcat/package.xml").to_dp()
    )
    assert package.title == "Fishway_Obstruction_Data_v1.csv"
    assert package.version == "v1"
    assert package.description
    assert package.description.startswith("This dataset contains pool-weir type fishway")
    assert package.identifier == "https://doi.org/10.5281/zenodo.5770714"
    assert len(package.keywords) == 8
    assert package.keywords[0] == "fishways"
    assert len(package.distributions) == 2
    assert (
        package.distributions[0].download_url
        == "https://zenodo.org/records/5770714/files/Fishway_Obstruction_Data_v1.csv"
    )
    assert package.distributions[0].byte_size == 1377
    assert package.distributions[0].media_type == "text/csv"


def test_dcat_package_from_graph_round_trip():
    package = DcatPackage.from_graph(
        DcatPackage.from_path("data/plugins/dcat/package.xml").to_graph()
    )
    assert package.title == "Fishway_Obstruction_Data_v1.csv"
    assert package.version == "v1"
    assert package.description
    assert package.description.startswith("This dataset contains pool-weir type fishway")
    assert package.issued == "2021"
    assert package.is_version_of == ["https://doi.org/10.5281/zenodo.5770713"]
    assert package.identifier == "https://doi.org/10.5281/zenodo.5770714"
    assert package.languages == [
        "http://publications.europa.eu/resource/authority/language/ENG"
    ]
    assert package.pages == ["https://doi.org/10.5281/zenodo.5770714"]
    assert len(package.keywords) == 8
    assert package.keywords[0] == "fishways"
    assert len(package.distributions) == 3
    assert (
        package.distributions[1].download_url
        == "https://zenodo.org/records/5770714/files/Fishway_Obstruction_Data_v1.csv"
    )
    assert package.distributions[1].byte_size == 1377
    assert package.distributions[1].media_type == "text/csv"


def test_dcat_package_to_text():
    text = DcatPackage.from_path("data/plugins/dcat/package.xml").to_text(format="xml")
    assert text.startswith("<?xml")
