# Validating Metadata

In the Data Package Library metadata validation is separated from Metadata Modeling. If you have a metadata descriptor or you exported it from a model, you can validate it against JSONSchema based on the Data Package Standard validation rules. This validation is stricter than models validation and it also supports custom profiles defined as per the Data Package Standard.

!!! note

    Most examples here use `Schema` metadata class but it is also applicable to other classes

## Validating from a Path

It can be validated from local or remote descriptor:

```python
from dplib.actions.schema.check import check_schema

errors = check_schema('data/schema.json')
# if there are errors it will contain `dplib.errors.MetadataError`
```

## Validating from a Dict

A Python dictionary can be passed to the validator

```python
from dplib.actions.schema.check import check_schema

errors = check_schema({"missingValues": "-"})
# it will contain `dplib.errors.MetadataError`
```

## Validating a Model

It's also possible to validate a model:

```python
from dplib.models import Schema, Field
from dplib.actions.schema.check import check_schema

schema = Schema()
schema.add_field(Field(name='string', type='string'))
schema.profile = '<my-custom-profile-url>'
errors = check_schema(schema)
# if there are errors it will contain `dplib.errors.MetadataError`
```
