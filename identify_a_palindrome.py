def is_palindrome(string):
    string = "".join(string.split(" "))
    length = len(string) // 2
    for i in range(length):
        if string[i] != string[-(i+1)]:
            return False
    return True


def print_is_palindrome(inp):
    print(inp, is_palindrome(inp))


def main():
    print_is_palindrome("hello world")
    print_is_palindrome("anita lava la tina")
    print_is_palindrome("ama")
    print_is_palindrome("emme")
    print_is_palindrome("hi")


if __name__ == "__main__":
    main()
