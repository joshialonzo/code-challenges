from code_challenges.strings.ex_oh import ex_oh


def test_ex_oh_truthy():
    string = "xooxxo"
    assert ex_oh(string)


def test_ex_oh_falsy():
    string = "x"
    assert not ex_oh(string)
