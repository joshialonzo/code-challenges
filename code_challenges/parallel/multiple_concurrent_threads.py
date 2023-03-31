"""Threads that waste CPU cycles"""


import os
import threading


def cpu_waster():
    """A simple function that wastes CPU cycles forever"""
    while True:
        pass

# display information about this process
print("\n Process ID: ", os.getpid())
print("Thread count: ", threading.active_count())
for thread in threading.enumerate():
    print(thread)


print("\n Starting 12 CPU wasters...")
for i in range(12):
    threading.Thread(target=cpu_waster).start()


# display information about this process
print("\n Process ID: ", os.getpid())
print("Thread count: ", threading.active_count())
for thread in threading.enumerate():
    print(thread)
