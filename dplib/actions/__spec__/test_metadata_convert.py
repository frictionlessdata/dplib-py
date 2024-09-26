import pytest

from dplib.actions.metadata.convert import convert_metadata


@pytest.mark.parametrize(
    "source,target",
    (
        ("bad", "ckan"),
        ("ckan", "bad"),
    ),
)
def test_convert_metadata_bad_source_or_target_dp_012(source: str, target: str):
    with pytest.raises(ValueError):
        convert_metadata("resource.json", type="resource", source=source, target=target)  # type: ignore
