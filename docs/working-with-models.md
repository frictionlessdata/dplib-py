# Working with Models

Data Package Library comes with Pydantic models covering all the metadata classes defined in the [Data Package Standard](https://datapackage.org)

## Creating a Model

You can create a model from scratch:

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

Or loaded from a text or dictionary:

```python
from dplib.models import Schema

schema = Schema.from_text('{"fields": []}', format='json')
schema = Schema.from_dict({"fields": []})
```
