# Dialect

The Table Dialect model allows to manipulate a Pydantic model in Python according to the [Table Dialect specification](https://datapackage.org/specifications/table-dialect/)

## Usage

```python
from dplib.models import Dialect

dialect = Dialect()
dialect.delimiter = ';'
dialect.header = False
print(dialect.to_text(format="json"))
```

```json
{
  "delimiter": ";",
  "header": false
}
```

## Reference

::: dplib.models.Dialect
