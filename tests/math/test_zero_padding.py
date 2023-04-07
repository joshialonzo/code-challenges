import pytest
from code_challenges.math.binary.zero_padding import pad


def test_zero_padding_1():
    binary, places = "1", 8
    assert pad(binary, places) == "00000001"


def test_zero_padding_2():
    binary, places = "10", 8
    assert pad(binary, places) == "00000010"


def test_zero_padding_3():
    binary, places = "11", 8
    assert pad(binary, places) == "00000011"


def test_zero_padding_4():
    binary, places = "100", 8
    assert pad(binary, places) == "00000100"


def test_zero_padding_5():
    binary, places = "101", 8
    assert pad(binary, places) == "00000101"


def test_zero_padding_error():
    binary, places = "11111", 4
    with pytest.raises(ValueError):
        pad(binary, places)
