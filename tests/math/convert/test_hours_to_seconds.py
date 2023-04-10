from code_challenges.math.convert.hours.seconds import (
    to_seconds as convert_hours_to_seconds,
)


def test_hours_to_seconds_10():
    hours = 10
    assert convert_hours_to_seconds(hours)


def test_hours_to_seconds_1():
    hours = 1
    assert convert_hours_to_seconds(hours)


def test_hours_to_seconds_2_5():
    hours = 2.5
    assert convert_hours_to_seconds(hours)


def test_hours_to_seconds_100():
    hours = 100
    assert convert_hours_to_seconds(hours)


def test_hours_to_seconds_33():
    hours = 33
    assert convert_hours_to_seconds(hours)
