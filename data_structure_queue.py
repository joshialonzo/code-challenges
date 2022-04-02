import queue


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """Takes in an item and inserts that item into the 0th index of the list
        that is representing the queue.

        The runtime is O(n) or linear time, because inserting into the 0th index
        of a list forces all the other items in the list to move one index to the
        right.
        """
        self.items.insert(0, item)

    def dequeue(self):
        """Returns and removes the front-most item of the queue, which is
        represented by the last item in the queue.

        The runtime is O(1), or constant time, because indexing to the end of the
        list happens in constant time.
        """
        if self.items:
            return self.items.pop()
        return None

    def peek(self):
        """This method return the last item in the list, which is also the
        front-most item of the queue.
        
        This method runs in constant time because indexing into a list is
        done in constant time.
        """
        if  self.items:
            return self.items[-1]
        return None

    def size(self):
        """This method returns the lenght of the list that is representing the queue.
        
        This method runs in constant time because finding the length of a list also
        happens in constant time.
        """
        return len(self.items)

    def is_empty(self):
        """This method returns a boolean value describing whether or not the queue is
        empty.
        
        Testing for equality happens in constant time.
        """
        return self.items == []


def main():
    # create a queue
    queue = Queue()
    # add some items to the queue
    queue.enqueue("apple")
    queue.enqueue("banana")
    assert queue.items == ["banana", "apple"]
    # size of the queue
    assert queue.size() == 2
    # is the queue empty?
    assert queue.is_empty() == False
    # peek the next item in the queue
    assert queue.peek() == "apple"
    # remove an item from the queue
    queue.dequeue()
    assert queue.items == ["banana"]
    # remove all items from the queue
    queue.dequeue()
    queue.dequeue()
    assert queue.items == []
    # peek the next item in the queue
    assert queue.peek() == None
    # is the queue empty?
    assert queue.is_empty() == True
    # size of the queue
    assert queue.size() == 0


if __name__ == "__main__":
    main()
