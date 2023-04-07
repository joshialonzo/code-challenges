def show_welcome_message():
    print("Welcome to the GPA calculator.")
    print("Please, enter all your letter grades in one line separated by space.")


def compute_grade_point_average(grades):
    grades = grades.split()
    points = {
        "A+": 4.0, "A": 4.0, "A-": 3.67,
        "B+": 3.33, "B": 3.0, "B-": 2.67,
        "C+": 2.33, "C": 2.0, "C-": 1.67,
        "D+": 1.33, "D": 1.0, "F": 0.0,
    }
    num_courses = 0
    total_points = 0
    for grade in grades:
        if grade in points:
            num_courses += 1
            total_points += points[grade]
        else:
            print(
                f"Unknown grade {grade} being ignored."
            )
    
    gpa = total_points / num_courses

    return gpa


def show_farewell_message(gpa):
    msg = f"Your GPA is {gpa}."
    print(msg)


def main():
    show_welcome_message()
    grades = input()
    gpa = compute_grade_point_average(grades)
    show_farewell_message(gpa)


if __name__ == "__main__":
    main()
