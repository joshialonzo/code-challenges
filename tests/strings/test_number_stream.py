from code_challenges.strings.number_stream import number_stream


def test_number_stream_truthy():
    string = "6539923335"
    assert number_stream(string)


def test_number_stream_falsy():
    string = "66633444"
    assert not number_stream(string)
