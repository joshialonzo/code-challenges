import ssl
from typing import Any


class SLLNode:
    
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
    
    def __repr__(self) -> str:
        return f"<SLLNode: data={self.data}>"

    def get_data(self) -> Any:
        """Return the self.data attribute."""
        return self.data

    def set_data(self, new_data) -> None:
        """Replace the existing value of the self.data attribute with new_data
        parameter.
        """
        self.data = new_data

    def get_next(self) -> Any:
        """Return the self.next attribute."""
        return self.next

    def set_next(self, new_next) -> None:
        """Replace the existing value of the self.next attribute with new_next
        parameter.
        """
        self.next = new_next
    

class SLL:

    def __init__(self) -> None:
        self.head = None
    
    def __repr__(self) -> str:
        return f"<SLL: head={self.head}>"
    
    def is_empty(self):
        """Returns True if the linked list is empty. Otherwise, returns False. """
        return self.head is None

    def add_front(self, new_data):
        """Add a node whose data is the new_data argument to the front of the linked list."""
        new_node = SLLNode(new_data)
        new_node.set_next(self.head)
        self.head = new_node

    def size(self):
        """Traverses the linked list and returns an integer value representing
        the number of nodes in the linked list.

        The time complexity is O(n) because every node in the linked list must
        be visited in order to calculate the size of the linked list.
        """
        _size = 0

        if self.head is None:
            return 0

        current = self.head
        # While there are still nodes left to count
        while current is not None:
            _size += 1
            current = current.get_next()
        
        return _size

    
    def search(self, data):
        """Traverses the linked list and returns True if the data searched for
        is present in one of the nodes. Otherwise, it returns False.

        The time complexity is O(n) because in the worst case we have to go to
        every node in order to find what we are looking for.
        """
        if self.head is None:
            return "Linked list is empty. No nodes to search."
        
        current = self.head
        while current is not None:
            # the node's data matches what we are looking for
            if current.get_data() == data:
                return True
            # the node's data does not match
            else:
                current = current.get_next()
        
        return False


    def remove(self, data):
        """Removes the first occurence of a node that contains the data argument
        as its self.data variable. Returns nothing.
        
        The time complexity is O(n) because in the worst case we have to visit
        every node before we find the one we need to remove.
        """
        if self.head is None:
            return "Linked list is empty. No nodes to remove."
        
        current = self.head
        previous = None
        found = False
        while not found:
            if current.get_data() == data:
                found = True
            else:
                if current.get_next() is None:
                    return "A node with that data value is not present."
                else:
                    previous = current
                    current = current.get_next()
        
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())


def main():
    # initial node with data
    node = SLLNode("apple")
    # verify the initial data
    assert node.get_data() == "apple"
    # change the data of the node
    node.set_data(7)
    assert node.get_data() == 7
    # create another node
    another_node = SLLNode("carrot")
    # set next node
    node.set_next(another_node)
    assert node.get_next() == another_node
    assert node.get_next().get_data() == "carrot"
    # create a singly linked list
    sll = SLL()
    assert sll.is_empty()
    assert sll.size() == 0
    # try to remove a node
    assert sll.remove("banana") == "Linked list is empty. No nodes to remove."
    # append node to the SLL
    sll.add_front("berry")
    assert sll.is_empty() == False
    assert sll.head.data == "berry"
    # append more nodes
    sll.add_front("banana")
    sll.add_front("carrot")
    assert sll.size() == 3
    # search for an element in the linked list
    assert sll.search("banana") == True
    assert sll.search("cocoa") == False
    # try to remove an element that does not exist
    assert sll.remove("orange") == "A node with that data value is not present."
    # remove the first element of the linked list
    sll.remove("berry")
    assert sll.head.get_data() == "carrot"
    # remove any element of the linked list
    sll.remove("carrot")
    sll.remove("carrot") == "A node with that data value is not present."

if __name__ == "__main__":
    main()
