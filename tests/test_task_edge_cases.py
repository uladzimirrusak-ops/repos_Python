import pytest


def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        _ = 1 / 0
