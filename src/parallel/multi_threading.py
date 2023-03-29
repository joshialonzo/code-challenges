"""
* Basic Multithreading
* Basic Multithreading with saving of the results
* Multiple threads with saving of the results
"""
import threading
import time


def long_square(num):
    """ Square of a number
        It takes a long time.
    """
    time.sleep(1)
    return num ** 2


def long_computation():
    """Long computation"""
    print(
        [long_square(n) for n in range(5)]
    )


def long_square_and_saving(num: int, results: dict):
    """ Square of a number
        It takes a long time.
    """
    time.sleep(1)
    results[num] = num ** 2


def multi_thread_computation():
    """Basic Multithreading"""
    t_1 = threading.Thread(target=long_square, args=(1,))
    t_2 = threading.Thread(target=long_square, args=(2,))

    t_1.start()
    t_2.start()

    t_1.join()
    t_2.join()


def multi_threading_computation_with_saving():
    """Basic Multithreading with saving of the results"""
    results = {}
    t_1 = threading.Thread(target=long_square_and_saving, args=(1, results))
    t_2 = threading.Thread(target=long_square_and_saving, args=(2, results))

    t_1.start()
    t_2.start()

    t_1.join()
    t_2.join()

    print(results)


def multiple_threads_with_saving():
    """Multiple threads with saving of the results"""
    results = {}
    threads = [
        threading.Thread(
            target=long_square_and_saving,
            args=(n, results)
        ) for n in range(0, 10)
    ]

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    print(results)


def main():
    "Main function"
    multiple_threads_with_saving()


if __name__ == "__main__":
    main()
