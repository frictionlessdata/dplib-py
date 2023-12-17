# Zenodo

Zenodo plugin provides Package and Resource models and converters between Zenodo and Data Package notations

## Installation

Not extra dependencies are required

## Usage

Converting a Zenodo descriptor to the Data Package notation:

```python
from dplib.plugins.zenodo.models import ZenodoPackage

package = ZenodoPackage.from_path("data/plugins/zenodo/package.json").to_dp()
print(package.to_text(format='json'))
```

```json
{
  "resources": [
    {
      "name": "fishway_obstruction_data_v1",
      "path": "Fishway_Obstruction_Data_v1.csv",
      "format": "csv",
      "mediatype": "text/csv",
      "bytes": 1377,
      "hash": "7bdef6756c84c3aea749f8211c557684"
    },
    {
      "name": "readme",
      "path": "readme.md",
      "format": "md",
      "mediatype": "application/octet-stream",
      "bytes": 1577,
      "hash": "a23a3c99befca45e706c9343e39f5926"
    }
  ],
  "id": "https://doi.org/10.5281/zenodo.5770714",
  "title": "Fishway_Obstruction_Data_v1.csv",
  "description": "<p>This dataset contains pool-weir type fishway (sumerged notch and orifice) hydraulic scenarios with and without obstruction events in accordance with&nbsp;the publication:&nbsp;</p>\n\n<p>Fuentes-P&eacute;rez, J.F., Garc&iacute;a-Vega, A., Bravo-C&oacute;rdoba, F.J., Sanz-Ronda, F.J. 2021. A Step to Smart Fishways: An Autonomous Obstruction Detection System Using Hydraulic Modeling and Sensor Networks. Sensors 2021, 21(20), 6909.</p>",
  "homepage": "https://zenodo.org/api/records/5770714",
  "version": "v1",
  "contributors": [
    {
      "title": "Fuentes-P\u00e9rez, Juan Francisco",
      "role": "personal",
      "organization": "Department of Hydraulics and Hydrology, ETSIIAA, University of Valladolid, 34004 Palencia, Spain"
    }
  ],
  "keywords": [
    "fishways",
    "hydraulics",
    "smart fishways",
    "pool-weir",
    "hydrological variability",
    "nonuniformity",
    "clogging",
    "water-level sensors"
  ],
  "created": "2021-12-10T05:47:07.709885+00:00"
}
```

Converting a Data Package to Zenodo notation:

```python
from dplib.models import Package
from dplib.plugins.zenodo.models import ZenodoPackage

package = ZenodoPackage.from_dp(Package.from_path("data/package.json"))
print(package.to_text(format="xml"))
```

## Reference

::: dplib.plugins.zenodo.models.ZenodoPackage

::: dplib.plugins.zenodo.models.ZenodoResource
