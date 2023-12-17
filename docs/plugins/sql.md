# SQL

SQL plugin provides Schema and Fields models and converters between SQL (in `sqlalchemy` terms) and Data Package notations

## Installation

Extra dependency needs to be installed:

```bash
pip install dplib-py[sql]
```

## Usage

Converting a SQL dataframe to the Data Package notation:

```python
from dplib.plugins.sql.models import SqlSchema

schema = SqlSchema(table=table).to_dp()
print(schema.to_text(format='json'))
```

Converting from Data Package notation to SQL:

```python
from dplib.models import Schema
from dplib.plugins.sql.models import SqlSchema

schema = SqlSchema.from_dp(Schema.from_path('data/schema.json'))
print(schema.table)
```

## Reference

::: dplib.plugins.sql.models.SqlSchema
::: dplib.plugins.sql.models.SqlField
