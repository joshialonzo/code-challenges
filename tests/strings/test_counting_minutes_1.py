from code_challenges.strings.counting_minutes_1 import counting_minutes_1


def test_counting_minutes_1320():
    string = "1:00pm-11:00am"
    assert counting_minutes_1(string) == 1320


def test_counting_minutes_1416():
    string = "2:03pm-1:39pm"
    assert counting_minutes_1(string) == 1416


def test_counting_minutes_712():
    string = "2:08pm-2:00am"
    assert counting_minutes_1(string) == 712


def test_counting_minutes_60():
    string = "2:00pm-3:00pm"
    assert counting_minutes_1(string) == 60


def test_counting_minutes_190():
    string = "11:00am-2:10pm"
    assert counting_minutes_1(string) == 190


def test_counting_minutes_825():
    string = "3:00pm-4:45am"
    assert counting_minutes_1(string) == 825


def test_counting_minutes_11():
    string = "5:00pm-5:11pm"
    assert counting_minutes_1(string) == 11
