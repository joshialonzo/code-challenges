from random import randrange


class PrintQueue:
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



class Job:
    def __init__(self, pages=None) -> None:
        self.pages = pages if pages else randrange(0, 11)
    
    def print_page(self):
        self.pages -= 1
    
    def check_complete(self):
        if self.pages == 0:
            return True
        return False


class Printer:

    def __init__(self) -> None:
        self.current_job = None

    def get_job(self, print_queue: PrintQueue):
        try:
            self.current_job = print_queue.dequeue()
        except IndexError:
            return "No more jobs to print."

    def print_job(self, job):
        while job.pages > 0:
            job.print_page()
        
        if job.check_complete():
            return "Printing complete."
        else:
            return "An error occured."


def main():
    # Create a job
    job_1 = Job()
    # Create a print queue
    print_q = PrintQueue()
    # Create a printer
    printer = Printer()

    # Append a job to the queue
    print_q.enqueue(job_1)
    assert print_q.size() == 1
    # Take a job to print
    printer.get_job(print_q)
    assert print_q.items == []
    # Print the status of the current job
    assert printer.print_job(printer.current_job) == "Printing complete."


if __name__ == "__main__":
    main()
