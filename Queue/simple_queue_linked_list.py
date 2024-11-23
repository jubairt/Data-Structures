class Node:
    def __init__(self, data) -> None:
        """Initialize a node with data and a pointer to the next node."""
        self.data = data
        self.next = None


class Queue:
    def __init__(self) -> None:
        """Initialize the queue with an empty head, tail, and count."""
        self.head = None
        self.tail = None
        self.count = 0

    def enqueue(self, data):
        """Add a new node with data to the end (tail) of the queue."""
        new_node = Node(data)
        self.count += 1
        if not self.head:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node  # Connect current tail to new node
            self.tail = new_node  # Move tail pointer to the new node

    def dequeue(self):
        """Remove and return the node from the front (head) of the queue."""
        if not self.head:
            raise IndexError("Queue Underflow")  # Raise error if queue is empty
        dequeued_value = self.head.data  # Get the data of the front node
        self.head = self.head.next  # Move head pointer to the next node
        self.count -= 1
        if self.head is None:  # If the queue becomes empty, reset tail to None
            self.tail = None
        return dequeued_value

    def isEmpty(self) -> bool:
        """Check if the queue is empty."""
        return self.head is None

    def peek(self):
        """Return the data of the front node without removing it."""
        if not self.head:
            return None
        return self.head.data

    def __len__(self) -> int:
        """Return the number of elements in the queue."""
        return self.count

    def __iter__(self):
        """Allow iteration over the queue."""
        temp = self.head
        while temp:
            yield temp.data  # Yield the data of the current node
            temp = temp.next  # Move to the next node


# Example usage
ll_queue = Queue()

# Enqueue some elements
ll_queue.enqueue(10)
ll_queue.enqueue(20)
ll_queue.enqueue(30)

# Print all elements in the queue
for i in ll_queue:
    print(i)
# Expected Output:
# 10
# 20
# 30

# Dequeue one element
ll_queue.dequeue()

# Print all remaining elements in the queue after one dequeue
for i in ll_queue:
    print(i)
# Expected Output:
# 20
# 30
