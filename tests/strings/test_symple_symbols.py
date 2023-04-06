from code_challenges.strings.simple_symbols import simple_symbols


def test_simple_symbols_truthy():
    string = "+d+=3=+s+"
    assert simple_symbols(string)


def test_simple_symbols_falsy():
    string = "f++d+"
    assert not simple_symbols(string)
