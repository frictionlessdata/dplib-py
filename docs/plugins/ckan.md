# CKAN

CKAN plugin provides Package and Resource models and converters between CKAN and Data Package notations

## Installation

Not extra dependencies are required

## Usage

Converting a CKAN descriptor to the Data Package notation:

```python
from dplib.plugins.ckan.models import CkanPackage

package = CkanPackage.from_path("data/plugins/ckan/package.json").to_dp()
print(package.to_text(format='json'))
```

```json
{
  "resources": [
    {
      "name": "sample_linked",
      "path": "sample-linked.csv",
      "format": "csv",
      "mediatype": "text/csv",
      "ckan:id": "e687245d-7835-44b0-8ed3-0827de123895"
    },
    {
      "name": "sample",
      "path": "sample.csv",
      "format": "csv",
      "mediatype": "application/csv",
      "bytes": 6731,
      "ckan:id": "b53c9e72-6b59-4cda-8c0c-7d6a51dad12a"
    },
    {
      "name": "views",
      "path": "views.csv",
      "format": "csv",
      "bytes": 32773,
      "ckan:id": "9ce6650b-6ff0-4a52-9b10-09cfc29bbd7e"
    },
    {
      "name": "sample",
      "path": "sample.pdf",
      "format": "pdf",
      "bytes": 712352,
      "ckan:id": "8aa53505-3b7f-4b9c-9b54-cf674eadc3f1"
    },
    {
      "name": "sample",
      "path": "sample.txt",
      "format": "txt",
      "bytes": 85,
      "ckan:id": "0185907b-2812-437f-9c64-eae24771ef5f"
    },
    {
      "name": "sample",
      "path": "sample.geojson",
      "format": "geojson",
      "bytes": 255943,
      "ckan:id": "ecd4a62d-998b-46e4-8a64-cadac2125c64"
    },
    {
      "name": "sample",
      "path": "sample.kml",
      "format": "kml",
      "bytes": 474000,
      "ckan:id": "048333ab-9608-42dc-901b-a7dd9fca3dda"
    },
    {
      "name": "avoid_crowds_when_buying_materials_social_media_post",
      "path": "avoid-crowds-when-buying-materials-social-media-post.jpeg",
      "format": "jpeg",
      "mediatype": "image/png",
      "bytes": 444695,
      "ckan:id": "b6c22c1d-e789-490d-b935-989093bbb173"
    },
    {
      "name": "sample_wms",
      "path": "Sample WMS",
      "format": "wms",
      "ckan:id": "664e5e2c-bd7d-4972-a245-a747f7d61cc9"
    }
  ],
  "name": "sample-dataset-1",
  "title": "Sample Dataset",
  "description": "A CKAN Dataset is a collection of data resources (such as files), together with a description and other information (what is known as metadata), at a fixed URL. \r\n\r\n",
  "version": "1.0",
  "licenses": [
    {
      "name": "cc-by",
      "title": "Creative Commons Attribution",
      "url": "http://www.opendefinition.org/licenses/cc-by"
    }
  ],
  "contributors": [
    {
      "title": "Test Author",
      "email": "test@email.com",
      "role": "author"
    },
    {
      "title": "Test Maintainer",
      "email": "test@email.com",
      "role": "maintainer"
    }
  ],
  "keywords": [
    "csv",
    "economy",
    "geojson",
    "kml",
    "pdf",
    "sample",
    "txt",
    "wms"
  ],
  "created": "2021-04-09T11:39:37.657233",
  "ckan:id": "c322307a-b871-44fe-a602-32ee8437ff04"
}
```

Converting a Data Package to CKAN notation:

```python
from dplib.models import Package
from dplib.plugins.ckan.models import CkanPackage

package = CkanPackage.from_dp(Package.from_path("data/package.json"))
print(package.to_text(format="json"))
```

## Reference

::: dplib.plugins.ckan.models.CkanPackage
::: dplib.plugins.ckan.models.CkanResource
