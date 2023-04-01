"""
Have the function FirstReverse(str) take the str parameter
being passed and return the string in reversed order.
For example: if the input string is "Hello World and Coders"
then your program should return the string "sredoC dna dlroW olleH".
"""

def first_reverse(string):
    """Reverse a string"""
    string = string[::-1]
    return string


def main():
    """Main function"""
    assert (
        first_reverse("Hello World and Coders")
        ==
        "sredoC dna dlroW olleH"
    )


if __name__ == "__main__":
    main()
