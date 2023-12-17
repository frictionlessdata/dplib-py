# Resource

The Data Resource model allows to manipulate a Pydantic model in Python according to the [Data Resource specification](https://datapackage.org/specifications/data-resource/)

## Usage

```python
from dplib.models import Resource, Schema, Field

resource = Resource()
resource.name = 'name'
resource.path = 'table.csv'
resource.schema = Schema(fields=[Field(name='id', type='integer')])
print(resource.to_text(format="json"))
```

```json
{
  "name": "name",
  "path": "table.csv",
  "schema": {
    "fields": [
      {
        "name": "id",
        "type": "integer"
      }
    ]
  }
}
```

## Reference

::: dplib.models.Resource
::: dplib.models.License
::: dplib.models.Source
::: dplib.models.Contributor
