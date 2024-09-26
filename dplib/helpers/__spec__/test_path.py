import pytest

from dplib.helpers.path import assert_safe_path


@pytest.mark.parametrize(
    "path",
    (
        "../data.csv",
        "/etc/home/secret.json",
        "http:test/../../secret.json",
    ),
)
def test_assert_safe_path_raises_dp_001(path: str):
    with pytest.raises(Exception):
        assert_safe_path(path)
