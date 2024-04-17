from dplib.models import AnyField, IntegerField


def test_field_defaults():
    field = AnyField()
    assert field.type == "any"
    assert field.missingValues == [""]


def test_field_constraints():
    field = IntegerField()
    field.constraints.minimum = 1
    assert field.constraints.minimum == 1
    assert field.to_dict() == {"constraints": {"minimum": 1}}
