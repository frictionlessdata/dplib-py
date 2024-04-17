import sqlalchemy as sa
from sqlalchemy.dialects import postgresql as pg

from dplib.models import Schema, StringField
from dplib.plugins.sql.models import SqlSchema


def test_sql_schema_from_dp():
    schema = SqlSchema.from_dp(
        Schema.from_path("data/schema-types.json"), table_name="test"
    )
    assert schema.table.name == "test"
    assert len(schema.table.columns) == 16
    assert schema.get_field_names() == [
        "any",
        "array",
        "boolean",
        "date",
        "date_year",
        "datetime",
        "duration",
        "geojson",
        "geopoint",
        "integer",
        "number",
        "object",
        "string",
        "time",
        "year",
        "yearmonth",
    ]
    assert schema.get_field_types() == [
        sa.Text,
        pg.JSONB,
        sa.Boolean,
        sa.Date,
        sa.Date,
        sa.DateTime,
        sa.Text,
        pg.JSONB,
        sa.Text,
        sa.Integer,
        sa.Numeric,
        pg.JSONB,
        sa.Text,
        sa.Time,
        sa.Integer,
        sa.Text,
    ]


def test_sql_schema_to_dp_round_trip():
    schema = SqlSchema.from_dp(
        Schema.from_path("data/schema-types.json"), table_name="test"
    ).to_dp()
    assert len(schema.fields) == 16
    assert schema.get_field_names() == [
        "any",
        "array",
        "boolean",
        "date",
        "date_year",
        "datetime",
        "duration",
        "geojson",
        "geopoint",
        "integer",
        "number",
        "object",
        "string",
        "time",
        "year",
        "yearmonth",
    ]
    assert schema.get_field_types() == [
        "string",
        "object",
        "boolean",
        "date",
        "date",
        "datetime",
        "string",
        "object",
        "string",
        "integer",
        "number",
        "object",
        "string",
        "time",
        "integer",
        "string",
    ]


def test_sql_schema_from_dp_with_string_constraints():
    field = StringField(name="string")
    field.constraints.minLength = 1
    field.constraints.enum = ["a", "b", "c"]
    field.constraints.pattern = "^[a-z]+$"
    schema = SqlSchema.from_dp(Schema(fields=[field]), table_name="test")
    assert len(schema.table.columns[0].constraints) == 2
    assert isinstance(schema.table.columns[0].type, sa.Enum)
