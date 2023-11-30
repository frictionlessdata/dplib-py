from dpspecs import Schema


def test_schema():
    schema = Schema(fields=[])
    assert schema.fields == []
