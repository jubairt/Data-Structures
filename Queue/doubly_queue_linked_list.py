class Node:
    def __init__(self, data) -> None:
        self.data = data  # Stores the data of the node
        self.next = None  # Pointer to the next node in the list
        self.prev = None  # Pointer to the previous node in the list


class DoublyQueue:
    def __init__(self) -> None:
        self.head = None  # Pointer to the first node
        self.tail = None  # Pointer to the last node
        self.count = 0  # Tracks the number of elements in the queue

    def insert_beg(self, data):
        """Inserts an element at the beginning of the deque."""
        new_node = Node(data)  # Create a new node
        self.count += 1
        if not self.head:  # If deque is empty
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head  # Link new node to the current head
            self.head.prev = new_node  # Link the old head back to the new node
            self.head = new_node  # Make the new node the head

    def insert_end(self, data):
        """Inserts an element at the end of the deque."""
        self.count += 1
        new_node = Node(data)  # Create a new node
        if not self.head:  # If deque is empty
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node  # Link the old tail to the new node
            new_node.prev = self.tail  # Link the new node back to the old tail
            self.tail = new_node  # Make the new node the tail

    def delete_beg(self):
        """Deletes an element from the beginning of the deque."""
        if not self.head:  # If deque is empty
            raise IndexError("Underflow")
        else:
            self.count -= 1
            self.head.next.prev = None  # Disconnect the old head node
            self.head = self.head.next  # Move the head pointer to the next node

    def delete_end(self):
        """Deletes an element from the end of the deque."""
        if not self.tail:  # If deque is empty
            raise OverflowError("Queue overflow")
        else:
            self.count -= 1
            self.tail.prev.next = None  # Disconnect the old tail node
            self.tail = self.tail.prev  # Move the tail pointer to the previous node

    def isEmpty(self):
        """Returns True if the deque is empty, else False."""
        return self.head == None

    def peek_first(self):
        """Returns the data of the first element in the deque."""
        if self.head:
            return self.head.data

    def peek_end(self):
        """Returns the data of the last element in the deque."""
        if self.tail:
            return self.tail.data

    def traverse(self):
        """Traverses and prints the elements of the deque."""
        if not self.head:  # If deque is empty
            return None
        temp = self.head
        while temp:
            print(f"{temp.data}", end="<->" if temp.next else "\n")  # Print data and link if not the last element
            temp = temp.next

    def __len__(self):
        """Returns the number of elements in the deque."""
        return self.count


# Example usage
dq = DoublyQueue()

# Checking if the deque is initially empty
print(dq.isEmpty())  # Expected: True

# Insert elements at the beginning and end
dq.insert_beg(10)
dq.insert_beg(5)
dq.insert_beg(1)
dq.insert_end(20)
dq.insert_end(50)

# Traversing the deque
dq.traverse()  # Expected: 1<->5<->10<->20<->50

# Deleting elements from the beginning and end
dq.delete_beg()  # Remove 1 from the beginning
dq.delete_end()  # Remove 50 from the end
dq.traverse()  # Expected: 5<->10<->20

# Peek at the first and last elements
print(dq.peek_end())  # Expected: 20
print(dq.peek_first())  # Expected: 5

# Get the number of elements in the deque
print(len(dq))  # Expected: 3
