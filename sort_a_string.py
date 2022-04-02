def sort_words(string):
    words = string.split()
    sorted_words = sorted(
        words,
        key=str.lower
    )
    sorted_string = " ".join(
        sorted_words
    )
    return sorted_string


def print_sort_words(string):
    print(f"Inp: {string} - Out: {sort_words(string)}")


def main():
    print_sort_words("hello world")
    print_sort_words("anita lava la tina")
    print_sort_words("This is a test string from Andrew")
    print_sort_words("banana ORANGE apple")

if __name__ == "__main__":
    main()
