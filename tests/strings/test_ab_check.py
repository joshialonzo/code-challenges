from code_challenges.strings.ab_check import ab_check


def test_ab_check_truthy():
    string = "Laura sobs"
    assert ab_check(string)


def test_ab_check_falsy():
    string = "after badly"
    assert not ab_check(string)


def test_ab_check_bzzza():
    string = "bzzza"
    assert ab_check(string)
