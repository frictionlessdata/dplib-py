from dplib.models import Field


def test_field_defaults():
    field = Field()
    assert field.type == "any"
    assert field.missingValues == [""]


def test_field_constraints():
    field = Field()
    field.constraints.minimum = 1
    assert field.constraints.minimum == 1
    assert field.to_dict() == {"constraints": {"minimum": 1}}
