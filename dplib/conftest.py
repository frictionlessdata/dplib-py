# type: ignore
import os

import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--ci",
        action="store_true",
        dest="ci",
        default=False,
        help="enable integrational tests",
    )


@pytest.fixture(scope="module")
def vcr_cassette_dir():
    return os.path.join("data", "cassettes")
