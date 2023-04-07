from code_challenges.math.binary.to_decimal import (
    to_decimal as binary_to_decimal
)


def test_binary_to_decimal_1():
    binary_number = "1"
    assert binary_to_decimal(binary_number) == 1


def test_binary_to_decimal_2():
    binary_number = "10"
    assert binary_to_decimal(binary_number) == 2


def test_binary_to_decimal_3():
    binary_number = "11"
    assert binary_to_decimal(binary_number) == 3


def test_binary_to_decimal_4():
    binary_number = "100"
    assert binary_to_decimal(binary_number) == 4


def test_binary_to_decimal_5():
    binary_number = "101"
    assert binary_to_decimal(binary_number) == 5
