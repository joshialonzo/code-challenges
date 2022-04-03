from multiprocessing.context import assert_spawning


class Deque:

    def __init__(self) -> None:
        self.items = []

    def add_front(self, item) -> None:
        """Takes an item as a parameter and inserts it into th 0th index
        of the list that is representing the deque.

        The runtime is linear or O(n), because every time you insert into
        the front of a list, all the other items in the list need to shift
        one position to the right.
        """
        self.items.insert(0, item)

    def add_rear(self, item) -> None:
        """Takes an item as a parameter and appends that item to the end of
        the list that is representing the deque.

        The runtime is constant because appending to the end of list happens
        in constant time.
        """
        self.items.append(item)

    def remove_front(self):
        """Removes and returns the item in the 0th index of the list, wich
        represents the front of the deque.

        The runtime is linear, or O(n) because when we remove an item from the
        0th index, all the other items have to shift one index to the left.
        """
        if self.items:
            return self.items.pop(0)
        return None

    def remove_rear(self):
        """Removes and returns the last item of the list, which represents the
        rear ot the deque.

        The runtime is constant because all we're doing is indexing to the end
        of the list.
        """
        if self.items:
            return self.items.pop()
        return None

    def peek_front(self):
        """This method return the first item in the list, which is also the
        front of the deque.
        
        This method runs in constant time because indexing into a list is
        done in constant time.
        """
        if self.items:
            return self.items[0]
        return None

    def peek_rear(self):
        """This method return the list item in the list, which is also the
        rear of the deque.
        
        This method runs in constant time because indexing into a list is
        done in constant time.
        """
        if self.items:
            return self.items[-1]
        return None

    def size(self):
        """This method returns the lenght of the list that is representing the deque.
        
        This method runs in constant time because finding the length of a list also
        happens in constant time.
        """
        return len(self.items)

    def is_empty(self):
        """This method returns a boolean value describing whether or not the deque is
        empty.
        
        Testing for equality happens in constant time.
        """
        return self.items == []


def main():
    # create a deque
    deque = Deque()
    # add an item to the front
    deque.add_front("apple")
    deque.add_front("orange")
    assert deque.items == ["orange", "apple"]
    # add an item to the rear
    deque.add_rear("banana")
    assert deque.items == ["orange", "apple", "banana"]
    # size of the deque
    assert deque.size() == 3
    # is the deque empty?
    assert deque.is_empty() == False
    # peek left-most item
    assert deque.peek_front() == "orange"
    # peek right-most item
    assert deque.peek_rear() == "banana"
    # remove an item from the front
    deque.remove_front()
    assert deque.items == ["apple", "banana"]
    # remove an item from the back
    deque.remove_rear()
    assert deque.items == ["apple"]
    # peek left-most item
    deque.remove_rear()
    assert deque.peek_front() == None
    # peek right-most item
    deque.remove_rear()
    assert deque.peek_rear() == None
    # size of the deque
    assert deque.size() == 0
    # is the deque empty?
    assert deque.is_empty() == True


if __name__ == "__main__":
    main()
