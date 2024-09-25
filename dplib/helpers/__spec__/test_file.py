import os
import stat
from pathlib import Path

from dplib.helpers.file import write_file


def test_write_file_permissions_dp_002(tmpdir: Path):
    path = str(tmpdir / "test.txt")
    write_file(path, "Hello, World!")
    mode = oct(stat.S_IMODE(os.stat(path).st_mode))
    assert mode == "0o600"
