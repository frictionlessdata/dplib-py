# Github

Github plugin provides Package and Resource models and converters between Github and Data Package notations

## Installation

Extra dependency needs to be installed:

```bash
pip install dplib-py[github]
```

## Usage

Converting a Github descriptor to the Data Package notation:

```python
from dplib.plugins.github.models import GithubPackage

package = GithubPackage.from_path("data/plugins/github/package.json").to_dp()
print(package.to_text(format='json'))
```

```json
{
  "name": "octocat/Hello-World",
  "title": "Hello-World",
  "description": "This your first repo!",
  "homepage": "https://github.com/octocat/Hello-World",
  "licenses": [
    {
      "name": "MIT",
      "title": "MIT License"
    }
  ],
  "keywords": ["octocat", "atom", "electron", "api"],
  "created": "2011-01-26T19:01:12Z"
}
```

Converting a Data Package to Github notation:

```python
from dplib.models import Package
from dplib.plugins.github.models import GithubPackage

package = GithubPackage.from_dp(Package.from_path("data/package.json"))
print(package.to_text(format="xml"))
```

## Reference

::: dplib.plugins.github.models.GithubPackage

::: dplib.plugins.github.models.GithubResource
