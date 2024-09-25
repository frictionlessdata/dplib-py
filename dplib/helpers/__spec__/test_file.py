import os
import stat
from pathlib import Path

from dplib.helpers.file import write_file


def test_write_file_implicit_permissions_dp_002(tmpdir: Path):
    path = str(tmpdir / "test.txt")
    write_file(path, "Hello, World!")
    permissions = oct(stat.S_IMODE(os.stat(path).st_mode))
    assert permissions == "0o600"


def test_write_file_explicit_permissions_dp_003(tmpdir: Path):
    path = str(tmpdir / "test.txt")
    write_file(path, "Hello, World!", permissions=0o644)
    permissions = oct(stat.S_IMODE(os.stat(path).st_mode))
    assert permissions == "0o644"
