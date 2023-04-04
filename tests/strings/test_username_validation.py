from code_challenges.strings.username_validation import username_validation


def test_strings_username_validation_falsy():
    username = "aa_"
    assert not username_validation(username)


def test_strings_username_validation_truthy():
    username = "u__hello_world123"
    assert username_validation(username)
