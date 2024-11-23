from typing import Optional

class Queue:
    def __init__(self, size) -> None:
        self.queue = [None] * size  # Initializes the queue with a fixed size
        self.rear = 0  # Points to the position of the next element to be added
        self.front = 0  # Points to the position of the next element to be removed
        self.count = 0  # Tracks the number of elements in the queue
        self.size = size  # Maximum size of the queue

    def enqueue(self, data):
        """Insert an element at the rear of the queue."""
        if self.isFull():
            raise OverflowError("Queue is full")  # Prevent adding if the queue is full
        self.queue[self.rear] = data
        self.rear = (self.rear + 1) % self.size  # Wrap around to the front if the rear reaches the end
        self.count += 1

    def dequeue(self) -> Optional[int]:
        """Remove and return an element from the front of the queue."""
        if self.isEmpty():
            raise IndexError("Dequeue from an empty queue")  # Prevent removal if the queue is empty
        deleted_value = self.queue[self.front]
        self.queue[self.front] = None  # Clear the position in the queue
        self.front = (self.front + 1) % self.size  # Wrap around to the front if the front reaches the end
        self.count -= 1
        return deleted_value

    def isEmpty(self) -> bool:
        """Check if the queue is empty."""
        return self.count == 0

    def isFull(self) -> bool:
        """Check if the queue is full."""
        return self.count == self.size

    def peek(self) -> Optional[int]:
        """Return the element at the front of the queue without removing it."""
        if self.isEmpty():
            return None
        return self.queue[self.front]

    def __len__(self) -> int:
        """Return the current number of elements in the queue."""
        return self.count

    def __iter__(self):
        """Iterate over the elements in the queue."""
        if self.isEmpty():
            return iter([])  # Return an empty iterator if the queue is empty
        idx = self.front
        for _ in range(self.count):
            yield self.queue[idx]
            idx = (idx + 1) % self.size  # Wrap around to the front if we reach the end

    def __str__(self) -> str:
        """Return a string representation of the queue's elements."""
        return ' '.join(str(i) for i in self)


# Example usage
queue = Queue(5)

# Try to print elements before adding anything
for i in queue:
    print(i)

# Enqueue some elements
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
queue.enqueue(50)

# Attempt to enqueue when the queue is full (this should raise an error)
try:
    queue.enqueue(8)
except OverflowError as e:
    print(e)  # Output: Queue is full

# Dequeue an element and print the state of the queue
queue.dequeue()

# Enqueue another element
queue.enqueue(0)

# Print the elements of the queue
for i in queue:
    print(i)

# Print the final state of the queue
print(queue)  # Output: 20 30 40 50 0
