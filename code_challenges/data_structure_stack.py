"""
Stack
* An ADT that stores items in the order in which they were added.
* Items are added to and removed from the "top" of a stack.
* LIFO: Last-in First-out
* A Python list is used to do this implementation because:
    * is mutable
    * and stores an ordered collection of items.

Opertions:
* Add to the stack
* Remove from the stack
-----------------------
* Is the stack empty?
* How many items are in the stack?
* What is next to be removed?
"""


class Stack:
    """Data Structure: Stack"""
    def __init__(self) -> None:
        self.items = []
    
    def push(self, item):
        """Accept an item as a parameter and appends it to the end of the stack.
        Returns nothing.

        The runtime of this methods is O(1), or constant time, because appending
        to the end of a list happens in constant time.
        """
        self.items.append(item)

    def pop(self):
        """Removes and returns the last item of the list which is the last item of
        the stack.

        The runtime here is constant time, because all it does is index to the last
        item of the list.
        """
        if self.items:
            return self.items.pop()
        return None

    def peek(self):
        """This method return the last item in the list, which is also the
        top item of the stack.
        
        This method runs in constant time because indexing into a list is
        done in constant time.
        """
        if self.items:
            return self.items[-1]
        return None

    def size(self):
        """This method returns the lenght of the list that is representing the stack.
        
        This method runs in constant time because finding the length of a list also
        happens in constant time.
        """
        return len(self.items)

    def is_empty(self):
        """This method returns a boolean value describing whether or not the stack is
        empty.
        
        Testing for equality happens in constant time.
        """
        return not self.items


def main():
    """Script: main"""
    # create a new stack
    my_stack = Stack()
    # append some elements to the stack
    my_stack.push("apple")
    my_stack.push("banana")
    my_stack.push("carrot")
    assert my_stack.items == ["apple", "banana", "carrot"]
    # how many items we have in the stack
    assert my_stack.size() == 3
    # is the stack empty?
    assert not my_stack.is_empty()
    # remove the last item of the stack
    my_stack.pop()
    assert my_stack.items == ["apple", "banana"]
    # peek the next item
    assert my_stack.peek() == "banana"
    # remove all the items of the stack
    my_stack.pop()
    my_stack.pop()
    my_stack.pop()
    assert not my_stack.items
    # how many items we have in the stack
    assert my_stack.size() == 0
    # is the stack empty?
    assert my_stack.is_empty()


if __name__ == "__main__":
    main()
