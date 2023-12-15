from dplib.models import Profile


def test_profile_from_dict():
    data = {"metadataProfile": {"name": "name"}, "additionalProperties": False}
    profile = Profile.from_dict(data)
    assert profile.name == "name"


def test_profile_to_dict():
    profile = Profile()
    profile.name = "name"
    profile.jsonSchema["additionalProperties"] = False
    assert profile.to_dict() == {
        "metadataProfile": {"name": "name"},
        "additionalProperties": False,
    }
