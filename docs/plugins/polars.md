# Polars

Polars plugin provides Schema and Fields models and converters between Polars and Data Package notations

## Installation

Extra dependency needs to be installed:

```bash
pip install dplib-py[polars]
```

## Usage

Converting a Polars dataframe to the Data Package notation:

```python
from dplib.plugins.polars.models import PolarsSchema

schema = PolarsSchema(df=df).to_dp()
print(schema.to_text(format='json'))
```

Converting from Data Package notation to Polars:

```python
from dplib.models import Schema
from dplib.plugins.polars.models import PolarsSchema

schema = PolarsSchema.from_dp(Schema.from_path('data/schema.json'))
print(schema.df)
```

## Reference

::: dplib.plugins.polars.models.PolarsSchema
::: dplib.plugins.polars.models.PolarsField
