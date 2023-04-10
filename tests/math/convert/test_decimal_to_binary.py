from code_challenges.math.convert.decimal.to_binary import (
    to_binary as decimal_to_binary,
)


def test_decimal_to_binary_1():
    number = 1
    assert decimal_to_binary(number) == "1"


def test_decimal_to_binary_2():
    number = 2
    assert decimal_to_binary(number) == "10"


def test_decimal_to_binary_3():
    number = 3
    assert decimal_to_binary(number) == "11"


def test_decimal_to_binary_4():
    number = 4
    assert decimal_to_binary(number) == "100"
