from data_structure_deque import Deque


def check_palindrome(string):
    deque = Deque()
    for char in string:
        deque.add_rear(char)
    length = len(string) // 2
    for _ in range(length):
        first = deque.remove_front()
        last = deque.remove_rear()
        if first != last:
            return False
    return True


def main():
    assert check_palindrome("mom") == True
    assert check_palindrome("level") == True
    assert check_palindrome("kayak") == True
    assert check_palindrome("hello") == False
    assert check_palindrome("hi") == False

if __name__ == "__main__":
    main()
