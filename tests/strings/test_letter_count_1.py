from code_challenges.strings.letter_count_1 import letter_count_1


def test_letter_count_1_truthy():
    string = "Hello apple pie"
    assert letter_count_1(string) == "Hello"


def test_letter_count_1_falsy():
    string = "No words"
    assert letter_count_1(string) == -1
