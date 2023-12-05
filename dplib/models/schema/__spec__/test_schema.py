from dplib.models import Schema


def test_schema():
    schema = Schema(fields=[])
    assert schema.fields == []
