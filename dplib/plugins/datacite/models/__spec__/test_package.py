from dplib.models import Package
from dplib.plugins.datacite.models import DatacitePackage


def test_datacite_package():
    package = DatacitePackage.from_path("data/plugins/datacite/package.json")
    assert package.version == "4.2"
    assert package.language == "en-US"
    assert package.publisher == "DataCite"
    assert package.publicationYear == "2014"
    assert package.schemaVersion == "http://datacite.org/schema/kernel-4"
    assert len(package.creators) == 1
    assert package.creators[0].name == "Miller, Elizabeth"
    assert len(package.contributors) == 1
    assert package.contributors[0].name == "Starr, Joan"
    assert package.contributors[0].givenName == "Joan"
    assert package.contributors[0].familyName == "Starr"
    assert len(package.descriptions) == 1
    assert package.descriptions[0].descriptionType == "Abstract"
    assert len(package.identifiers) == 2
    assert package.identifiers[0].identifierType == "DOI"
    assert len(package.rightsList) == 1
    assert package.rightsList[0].lang == "en-US"
    assert len(package.subjects) == 1
    assert package.subjects[0].subject == "000 computer science"
    assert len(package.titles) == 2
    assert package.titles[0].title == "Full DataCite XML Example"


def test_datacite_package_to_dp():
    package = DatacitePackage.from_path("data/plugins/datacite/package.json").to_dp()
    assert package.id == "https://doi.org/https://doi.org/10.1234/example-full"
    assert package.title == "Full DataCite XML Example"
    assert (
        package.description
        == "XML example of all DataCite Metadata Schema v4.3 properties."
    )
    assert (
        package.homepage
        == "https://schema.datacite.org/meta/kernel-4.3/example/datacite-example-full-v4.3.xml"
    )
    assert package.version == "4.2"
    assert package.keywords == ["000 computer science"]
    assert len(package.contributors) == 2
    assert package.contributors[0].title == "Miller, Elizabeth"
    assert package.contributors[0].givenName == "Elizabeth"
    assert package.contributors[0].familyName == "Miller"
    assert package.contributors[1].title == "Starr, Joan"
    assert package.contributors[1].givenName == "Joan"
    assert package.contributors[1].familyName == "Starr"
    assert package.contributors[1].roles == ["ProjectLeader"]
    assert len(package.licenses) == 1
    assert package.licenses[0].path == "http://creativecommons.org/publicdomain/zero/1.0"


def test_datacite_package_from_dp():
    package = DatacitePackage.from_dp(Package.from_path("data/package-full.json"))
    assert package.version == "1.0"
    assert len(package.contributors) == 1
    assert package.contributors[0].name == "title"
    assert len(package.descriptions) == 1
    assert package.descriptions[0].description == "description"
    assert package.descriptions[0].descriptionType == "Abstract"
    assert len(package.identifiers) == 1
    assert package.identifiers[0].identifier == "http://example.com"
    assert package.identifiers[0].identifierType == "URL"
    assert len(package.subjects) == 2
    assert package.subjects[0].subject == "keyword1"
    assert len(package.titles) == 1
    assert package.titles[0].title == "title"


def test_datacite_package_from_dp_round_trip():
    package = DatacitePackage.from_dp(
        DatacitePackage.from_path("data/plugins/datacite/package.json").to_dp()
    )
    assert package.version == "4.2"
    assert len(package.creators) == 1
    assert package.creators[0].name == "Miller, Elizabeth"
    assert len(package.contributors) == 1
    assert package.contributors[0].name == "Starr, Joan"
    assert package.contributors[0].givenName == "Joan"
    assert package.contributors[0].familyName == "Starr"
    assert len(package.descriptions) == 1
    assert package.descriptions[0].descriptionType == "Abstract"
    assert len(package.identifiers) == 2
    assert package.identifiers[0].identifierType == "DOI"
    assert len(package.subjects) == 1
    assert package.subjects[0].subject == "000 computer science"
    assert len(package.titles) == 1
    assert package.titles[0].title == "Full DataCite XML Example"
