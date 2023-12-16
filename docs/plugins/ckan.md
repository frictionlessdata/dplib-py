# CKAN

CKAN plugin provides models to Package and Resource between CKAN and Data Package notations

## Installation

```bash
pip install dplib-py[ckan]
```

## Usage

Converting a CKAN descriptor to the Data Package notation:

```python
from dplib.plugins.ckan.models import CkanPackage

package = CkanPackage.from_path("data/plugins/ckan/package.json").to_dp()
```

Converting a Data Package to CKAN notation:

```python
from dplib.models import Package
from dplib.plugins.ckan.models import CkanPackage

package = CkanPackage.from_dp(Package.from_path("data/package.json"))
```

## Reference

::: dplib.plugins.ckan.models.CkanPackage

::: dplib.plugins.ckan.models.CkanResource
