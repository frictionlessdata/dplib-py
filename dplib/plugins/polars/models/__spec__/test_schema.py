import polars as pl

from dplib.models import Schema
from dplib.plugins.polars.models import PolarsSchema


def test_polars_schema_from_dp():
    schema = PolarsSchema.from_dp(Schema.from_path("data/schema-types.json"))
    assert len(schema.df.schema) == 16
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
        pl.Utf8,
        pl.List(pl.Null),
        pl.Boolean,
        pl.Date,
        pl.Date,
        pl.Datetime(time_unit="us"),
        pl.Duration(time_unit="us"),
        pl.Struct([pl.Field("", pl.Null)]),
        pl.List(pl.Null),
        pl.Int64,
        pl.Decimal(scale=0),
        pl.Struct([pl.Field("", pl.Null)]),
        pl.Utf8,
        pl.Time,
        pl.Int8,
        pl.List(pl.Null),
    ]


def test_polars_schema_to_dp_round_trip():
    schema = PolarsSchema.from_dp(Schema.from_path("data/schema-types.json")).to_dp()
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
        "array",
        "boolean",
        "date",
        "date",
        "datetime",
        "duration",
        "object",
        "array",
        "integer",
        "number",
        "object",
        "string",
        "time",
        "integer",
        "array",
    ]
