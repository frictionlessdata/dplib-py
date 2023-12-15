from dplib.models import Package
from dplib.plugins.github.models import GithubPackage, GithubResource


def test_github_package():
    package = GithubPackage.from_path("data/plugins/github/package.json")
    assert package.private is False
    assert package.name == "Hello-World"
    assert package.full_name == "octocat/Hello-World"
    assert package.html_url == "https://github.com/octocat/Hello-World"
    assert package.description == "This your first repo!"
    assert package.pushed_at == "2011-01-26T19:06:43Z"
    assert package.created_at == "2011-01-26T19:01:12Z"
    assert package.updated_at == "2011-01-26T19:14:43Z"
    assert package.topics == ["octocat", "atom", "electron", "api"]
    assert package.license
    assert package.license.key == "mit"
    assert package.owner
    assert package.owner.login == "octocat"


def test_github_package_to_dp():
    package = GithubPackage.from_path("data/plugins/github/package.json").to_dp()
    assert package.name == "octocat/Hello-World"
    assert package.title == "Hello-World"
    assert package.description == "This your first repo!"
    assert package.homepage == "https://github.com/octocat/Hello-World"
    assert len(package.licenses) == 1
    assert package.licenses[0].name == "MIT"
    assert package.licenses[0].title == "MIT License"
    assert package.keywords == ["octocat", "atom", "electron", "api"]
    assert package.created == "2011-01-26T19:01:12Z"


def test_github_package_to_dp_with_resources():
    github = GithubPackage.from_path("data/plugins/github/package.json")
    github.resources.append(
        GithubResource(name="table.csv", path="table.csv", size=100, sha="hash")
    )
    package = github.to_dp()
    assert len(package.resources) == 1
    resource = package.resources[0]
    assert resource.name == "table"
    assert resource.path == "table.csv"
    assert resource.bytes == 100
    assert resource.hash == "sha1:hash"


def test_ckan_package_from_dp():
    package = GithubPackage.from_dp(Package.from_path("data/package-full.json"))
    assert package.name == "title"
    assert package.description == "description"
    assert package.topics == ["keyword1", "keyword2"]
    assert package.license
    assert package.license.name == "title"
    assert package.license.spdx_id == "name"
    assert package.license.html_url == "path"
    assert len(package.resources) == 1
    assert package.resources[0].name == "table.csv"
    assert package.resources[0].path == "table.csv"


def test_github_package_from_dp_round_trip():
    package = GithubPackage.from_dp(
        GithubPackage.from_path("data/plugins/github/package.json").to_dp()
    )
    assert package.name == "Hello-World"
    assert package.description == "This your first repo!"
    assert package.topics == ["octocat", "atom", "electron", "api"]
    assert package.license
    assert package.license.name == "MIT License"
