# Package

The Data Package model allows to manipulate a Pydantic model in Python according to the [Data Package specification](https://datapackage.org/specifications/data-package/)

## Usage

```python
from dplib.models import Package, Resource

package = Package()
package.name = 'name'
package.add_resource(Resource(name='table', path='table.csv'))
print(package.to_text(format="json"))
```

```json
{
  "resources": [
    {
      "name": "table",
      "path": "table.csv"
    }
  ],
  "name": "name"
}
```

## Reference

::: dplib.models.Package
::: dplib.models.License
::: dplib.models.Source
::: dplib.models.Contributor
