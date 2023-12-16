# Pandas

Pandas plugin provides Schema and Fields models and converters between Pandas and Data Package notations

## Installation

Extra dependency needs to be installed:

```bash
pip install dplib-py[pandas]
```

## Usage

Converting a Pandas dataframe to the Data Package notation:

```python
from dplib.plugins.pandas.models import PandasSchema

schema = PandasSchema(df=df).to_dp()
print(schema.to_text(format='json'))
```

Converting from Data Package notation to Pandas:

```python
from dplib.models import Schema
from dplib.plugins.pandas.models import PandasSchema

schema = PandasSchema.from_dp(Schema.from_path('data/schema.json'))
print(schema.df)
```

## Reference

::: dplib.plugins.pandas.models.PandasSchema
::: dplib.plugins.pandas.models.PandasField
