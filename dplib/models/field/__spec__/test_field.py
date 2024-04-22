from dplib.models import AnyField, IntegerField, StringField


def test_field_defaults():
    field = AnyField()
    assert field.type == "any"
    assert field.missingValues == [""]


def test_field_constraints():
    field = IntegerField()
    field.constraints.minimum = 1
    assert field.constraints.minimum == 1
    assert field.to_dict() == {
        "type": "integer",
        "constraints": {"minimum": 1},
    }


def test_field_to_dict():
    field = StringField(name="name")
    assert field.to_dict() == {
        "name": "name",
        "type": "string",
    }
