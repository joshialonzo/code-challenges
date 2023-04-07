from code_challenges.strings.dash_insert import dash_insert


def test_dash_insert_1():
    """
    Input: 99946
    Output: 9-9-946
    """
    string = "99946"
    assert dash_insert(string) == "9-9-946"


def test_dash_insert_1():
    """
    Input: 56730
    Output: 567-30
    """
    string = "56730"
    assert dash_insert(string) == "567-30"
