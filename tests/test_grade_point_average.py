from code_challenges.grade_point_average import compute_grade_point_average


def test_compute_grade_point_average_1():
    grades = "A"
    assert compute_grade_point_average(grades) == 4.0


def test_compute_grade_point_average_2():
    grades = "A+"
    assert compute_grade_point_average(grades) == 4.0


def test_compute_grade_point_average_3():
    grades = "A  A+"
    assert compute_grade_point_average(grades) == 4.0


def test_compute_grade_point_average_4():
    grades = "A  B  C"
    assert compute_grade_point_average(grades) == 3.0
