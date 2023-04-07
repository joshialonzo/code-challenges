from code_challenges.strings.username_validation import username_validation


def test_strings_username_validation_truthy():
    username = "u__hello_world123"
    assert username_validation(username)

def test_strings_username_validation_falsy_1():
    username = "aa_"
    assert not username_validation(username)


def test_strings_username_validation_falsy_2():
    username = "oooooooooooooooooo________a"
    assert not username_validation(username)


def test_strings_username_validation_falsy_3():
    username = "a______b_________555555555555aaaa"
    assert not username_validation(username)
