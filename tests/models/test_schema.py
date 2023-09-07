from dpspecs import Schema


def test_error():
    schema = Schema(fields=[])
    assert schema.fields == []
