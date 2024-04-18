# Schema

The Table Schema model allows to manipulate a Pydantic model in Python according to the [Table Schema specification](https://datapackage.org/specifications/table-schema/)

## Usage

```python
from dplib.models import Schema, IntegerField

schema = Schema()
schema.add_field(IntegerField(name='id'))
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
::: dplib.models.IFieldsMatch
::: dplib.models.ForeignKey
::: dplib.models.ForeignKeyReference
::: dplib.models.BaseField
::: dplib.models.Field
::: dplib.models.AnyField
::: dplib.models.ArrayField
::: dplib.models.BooleanField
::: dplib.models.DateField
::: dplib.models.DatetimeField
::: dplib.models.DurationField
::: dplib.models.GeojsonField
::: dplib.models.GeopointField
::: dplib.models.IntegerField
::: dplib.models.ListField
::: dplib.models.NumberField
::: dplib.models.ObjectField
::: dplib.models.StringField
::: dplib.models.TimeField
::: dplib.models.YearField
::: dplib.models.YearmonthField
::: dplib.models.BaseConstraints
::: dplib.models.CollectionConstraints
::: dplib.models.JsonConstraints
::: dplib.models.StringConstraints
::: dplib.models.ValueConstraints
