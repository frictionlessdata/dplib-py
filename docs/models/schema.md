# Schema

The Table Schema model allows to manipulate a Pydantic model in Python according to the [Table Schema specification](https://datapackage.org/specifications/table-schema/)

## Usage

```python
from dplib.models import Schema, Field

schema = Schema()
schema.add_field(Field(name='id', type='integer'))
schema.missingValues = ['-']
print(schema.to_text(format="json"))
```

```json
{
  "fields": [
    {
      "name": "id",
      "type": "integer"
    }
  ],
  "missingValues": ["-"]
}
```

## Reference

::: dplib.models.Schema
::: dplib.models.Field
::: dplib.models.Constraints
::: dplib.models.ForeignKey
::: dplib.models.ForeignKeyReference
