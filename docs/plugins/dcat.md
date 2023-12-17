# DCAT

DCAT plugin provides Package and Resource models and converters between DCAT and Data Package notations

## Installation

Extra dependency needs to be installed:

```bash
pip install dplib-py[dcat]
```

## Usage

Converting a DCAT descriptor to the Data Package notation:

```python
from dplib.plugins.dcat.models import DcatPackage

package = DcatPackage.from_path("data/plugins/dcat/package.xml").to_dp()
print(package.to_text(format='json'))
```

```json
{
  "resources": [
    {
      "name": "fishway_obstruction_data_v1",
      "path": "https://zenodo.org/records/5770714/files/Fishway_Obstruction_Data_v1.csv",
      "mediatype": "text/csv",
      "bytes": 1377
    },
    {
      "name": "readme",
      "path": "https://zenodo.org/records/5770714/files/readme.md",
      "bytes": 1577
    }
  ],
  "id": "https://doi.org/10.5281/zenodo.5770714",
  "title": "Fishway_Obstruction_Data_v1.csv",
  "description": "This dataset contains pool-weir type fishway (sumerged notch and orifice) hydraulic scenarios with and without obstruction events in accordance with\u00a0the publication:\u00a0 Fuentes-P\u00e9rez, J.F., Garc\u00eda-Vega, A., Bravo-C\u00f3rdoba, F.J., Sanz-Ronda, F.J. 2021. A Step to Smart Fishways: An Autonomous Obstruction Detection System Using Hydraulic Modeling and Sensor Networks. Sensors 2021, 21(20), 6909.",
  "version": "v1",
  "keywords": [
    "fishways",
    "hydraulics",
    "smart fishways",
    "pool-weir",
    "hydrological variability",
    "nonuniformity",
    "clogging",
    "water-level sensors"
  ]
}
```

Converting a Data Package to DCAT notation:

```python
from dplib.models import Package
from dplib.plugins.dcat.models import DcatPackage

package = DcatPackage.from_dp(Package.from_path("data/package.json"))
print(package.to_text(format="xml"))
```

## Reference

::: dplib.plugins.dcat.models.DcatPackage

::: dplib.plugins.dcat.models.DcatResource
