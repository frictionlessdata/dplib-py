# Working with Models

Data Package Library comes with Pydantic models covering all the metadata classes defined in the [Data Package Standard](https://datapackage.org)

!!! note

    Most examples here use `Schema` model but it is also applicable to other models

## Creating a Model

A model can be created from scratch:

```python
from dplib.models import Schema, Field

schema = Schema()
schema.add_field(Field(name='string', type='string'))
```

## Loading a Model

It can be opened from local or remote descriptor:

```python
from dplib.models import Schema

schema = Schema.from_path('data/schema.json')
```

Or loaded from a text or a dictionary:

```python
from dplib.models import Schema

schema = Schema.from_text('{"fields": []}', format='json')
schema = Schema.from_dict({"fields": []})
```

## Model Validation

If the input metadata is not valid the model will raise a validation error:

```python
from dplib.models import Schema

schema = Schema.from_dict({"fields": 1})
# will raise pydantic.ValidationError
```

Simirarly, property assignments are validated runtime as well:

```python
from dplib.models import Schema

schema = Schema()
schema.missingValues = '-'  # expected list of strings
# will raise pydantic.ValidationError
```

If you need to work with invalid metadat fix it first before creating a model:

```python
from dplib.models import Schema

metadata = {"missingValues": '-'}
metadata['missingValues'] = ['-']
schema = Schema.from_dict(metadata)
# OK
```

## Exporting a Model

When you need to save or print the model it can be exported:

```python
from dplib.models import Schema

schema = Schema.from_path('data/schema.json')
schema.to_path('schema.json') # OR
schema.to_text(format='json') # OR
schema.to_dict()
```

## Extending Models

!!! warning

    Currently, it might be affected by [this Pydantic issue](https://github.com/pydantic/pydantic/issues/5165)

If you develop a Data Package Extension it's easy to create corresponding models on top of the Data Package Library:

```python
from typing import List
from dplib.models import Schema, Field


class ExtensionField(Field):
    prop1: str
    prop2: str


class ExtensionSchema(Schema):
    profile: Literal[<url>] = <url>
    fields: List[ExtensionField] = []


field = ExtensionField(prop1="a", prop2='b')
schema = ExtensionSchema(fields=[field])
```
