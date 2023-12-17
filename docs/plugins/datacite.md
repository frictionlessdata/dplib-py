# Datacite

Datacite plugin provides Package model and converters between Datacite and Data Package notations

## Installation

Not extra dependencies are required

## Usage

Converting a Datacite descriptor to the Data Package notation:

```python
from dplib.plugins.datacite.models import DatacitePackage

package = DatacitePackage.from_path("data/plugins/datacite/package.json").to_dp()
print(package.to_text(format='json'))
```

```json
{
  "id": "https://doi.org/https://doi.org/10.1234/example-full",
  "title": "Full DataCite XML Example",
  "description": "XML example of all DataCite Metadata Schema v4.3 properties.",
  "homepage": "https://schema.datacite.org/meta/kernel-4.3/example/datacite-example-full-v4.3.xml",
  "version": "4.2",
  "licenses": [
    {
      "path": "http://creativecommons.org/publicdomain/zero/1.0",
      "title": "Creative Commons Zero v1.0 Universal"
    }
  ],
  "contributors": [
    {
      "title": "Miller, Elizabeth",
      "role": "creator",
      "organization": "DataCite"
    },
    {
      "title": "Starr, Joan",
      "role": "ProjectLeader",
      "organization": "California Digital Library"
    }
  ],
  "keywords": ["000 computer science"]
}
```

Converting a Data Package to Datacite notation:

```python
from dplib.models import Package
from dplib.plugins.datacite.models import Datacite

package = Datacite.from_dp(Package.from_path("data/package.json"))
print(package.to_text(format="json"))
```

## Reference

::: dplib.plugins.datacite.models.DatacitePackage
