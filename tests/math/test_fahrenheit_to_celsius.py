from code_challenges.math.fahrenheit.celsius import (
    to_celsius as fahrenheit_to_celsius,
)


def test_fahrenheit_to_celsius_1():
    degrees = 100
    assert fahrenheit_to_celsius(degrees) == 37.78


def test_fahrenheit_to_celsius_2():
    degrees = 88
    assert fahrenheit_to_celsius(degrees) == 31.11


def test_fahrenheit_to_celsius_3():
    degrees = 104
    assert fahrenheit_to_celsius(degrees) == 40.0


def test_fahrenheit_to_celsius_4():
    degrees = 112
    assert fahrenheit_to_celsius(degrees) == 44.44
