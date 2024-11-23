class Deque:
    def __init__(self, size):
        """Initialize the deque with a given size."""
        self.size = size
        self.deque = [None] * size
        self.front = -1
        self.rear = -1

    def is_full(self):
        """Check if the deque is full."""
        return (self.front == 0 and self.rear == self.size - 1) or (self.front == self.rear + 1)

    def is_empty(self):
        """Check if the deque is empty."""
        return self.front == -1

    def insert_front(self, item):
        """Insert an element at the front of the deque."""
        if self.is_full():
            print("Deque is full. Cannot insert at the front.")
            return
        if self.is_empty():
            self.rear = self.front = 0
        else:
            if self.front == 0:
                self.front = self.size - 1
            else:
                self.front -= 1
        self.deque[self.front] = item

    def insert_rear(self, item):
        """Insert an element at the rear of the deque."""
        if self.is_full():
            print("Deque is full")
            return
        if self.is_empty():
            self.rear = self.front = 0
        else:
            if self.rear == self.size - 1:
                self.rear = 0
            else:
                self.rear += 1
        self.deque[self.rear] = item

    def delete_front(self):
        """Delete an element from the front of the deque."""
        if self.is_empty():
            print("Queue is empty")
            return
        deleted_value = self.deque[self.front]
        self.deque[self.front] = None
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            if self.front == self.size - 1:
                self.front = 0
            else:
                self.front += 1
        return deleted_value

    def delete_rear(self):
        """Delete an element from the rear of the deque."""
        if self.is_empty():
            print("Queue is empty")
            return
        deleted_value = self.deque[self.rear]
        self.deque[self.rear] = None
        if self.rear == self.front:
            self.front = -1
            self.rear = -1
        else:
            if self.rear == 0:
                self.rear = self.size - 1
            else:
                self.rear -= 1
        return deleted_value

    def peek_front(self):
        """Peek the front element of the deque."""
        if self.is_empty():
            return None
        return self.deque[self.front]

    def peek_rear(self):
        """Peek the rear element of the deque."""
        if self.is_empty():
            return None
        return self.deque[self.rear]

    def traverse(self):
        """Traverse and print all elements in the deque."""
        if self.is_empty():
            print("Deque is empty")
            return
        current = self.front
        while current != self.rear:
            print(self.deque[current], end=" ")
            if current == self.size - 1:
                current = 0
            else:
                current += 1
        print(self.deque[current])  # Print the last element


# Example usage:
if __name__ == "__main__":
    deque = Deque(10)
    
    # Insert elements at both ends
    deque.insert_front(10)
    deque.insert_front(20)
    deque.insert_rear(30)
    deque.insert_rear(40)
    deque.insert_front(50)
    deque.insert_rear(99)
    deque.insert_front(33)
    deque.insert_rear(22)
    deque.insert_front(55)
    deque.insert_rear(66)
    deque.insert_front(77)
    deque.insert_rear(0)
    
    # Delete elements from both ends
    deque.delete_front()
    deque.delete_front()
    deque.delete_rear()
    
    # Insert new element
    deque.insert_front(89)
    
    # Traverse and print the current state of the deque
    deque.traverse()

# Output:
# 77 55 33 20 10 89 30 40 99 22
