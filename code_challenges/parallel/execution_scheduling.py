"""Two threads chopping vegetables"""


import threading
import time


chopping = True


def vegetable_chopper():
    name = threading.current_thread().getName()
    vegetable_count = 0
    while chopping:
        print(name, "chopped a vegetable")
        vegetable_count += 1
    print(name, "chopped", vegetable_count, "vegetables.")


if __name__ == "__main__":
    threading.Thread(target=vegetable_chopper, name="Joshi").start()
    threading.Thread(target=vegetable_chopper, name="Alonzi").start()

    time.sleep(1)
    chopping = False
