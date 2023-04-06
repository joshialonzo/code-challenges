from code_challenges.strings.question_marks import question_marks


def test_question_marks_truthy():
    string = "acc?7??sss?3rr1??????5"
    assert question_marks(string)


def test_question_marks_falsy_1():
    string = "aa6?9"
    assert not question_marks(string)


def test_question_marks_falsy_2():
    string = "9???1???9??1???9"
    assert not question_marks(string)


def test_question_marks_falsy_3():
    string = "5??aaaaaaaaaaaaaaaaaaa?5?5"
    assert not question_marks(string)
