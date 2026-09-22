import sys
from zoneinfo import ZoneInfo


def test_python_version() -> None:
    assert sys.version_info[:2] == (3, 11)


def test_seoul_timezone() -> None:
    assert ZoneInfo("Asia/Seoul").key == "Asia/Seoul"
