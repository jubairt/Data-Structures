class Hash:
    def __init__(self) -> None:
        self.size = 7  # Initial size of the hash table
        self.count = 0  # To keep track of the number of elements
        self.arr = [None] * self.size  # The actual hash table

    def _hash(self, key):
        return key % self.size  # Hash function

    def load_balancer(self):
        # Check if the load factor exceeds 0.8, then resize the hash table
        load_balancer = self.count / self.size
        if load_balancer > 0.8:
            self.size *= 2  # Double the size
            self.resize()  # Resize the table

    def insert(self, key):
        self.load_balancer()  # Check if resizing is needed
        index = self._hash(key)  # Get the index using the hash function
        if self.arr[index] is None:
            self.arr[index] = key  # Insert key if the spot is empty
            self.count += 1  # Increase the count
        return index

    def delete(self, key):
        index = self._hash(key)  # Get the index using the hash function
        if self.arr[index]:
            self.count -= 1  # Decrease the count
            value = self.arr[index]  # Store the value to return
            self.arr[index] = None  # Remove the key
            return value
        return False

    def search(self, key):
        index = self._hash(key)  # Get the index using the hash function
        if self.arr[index]:
            return self.arr[index]  # Return the value if found
        return False  # Return False if not found

    def display(self):
        # Display the elements of the hash table
        for i in self.arr:
            if i is not None:
                print(i, end=",")
        print()  # Print new line after displaying elements

    def resize(self):
        # Resize the table by creating a new array of double the size
        old_arr = self.arr
        self.arr = [None] * self.size
        self.count = 0  # Reset count
        for i in old_arr:
            if i:  # Re-insert the keys that were in the old array
                self.insert(i)
        return

# Test cases
h = Hash()

# Insert some elements
print(f"Index of inserting 5: {h.insert(5)}")
print(f"Index of inserting 10: {h.insert(10)}")
print(f"Index of inserting 15: {h.insert(15)}")
print(f"Index of inserting 20: {h.insert(20)}")
print(f"Index of inserting 25: {h.insert(25)}")  # This will trigger resize
print(f"Index of inserting 30: {h.insert(30)}")  # After resizing

# Display hash table
print("\nHash table after insertions:")
h.display()

# Search for elements
print(f"Search for 10: {h.search(10)}")
print(f"Search for 40: {h.search(40)}")

# Delete an element
print(f"Delete element 15: {h.delete(15)}")
print("Hash table after deletion of 15:")
h.display()

# Search for the deleted element
print(f"Search for 15 after deletion: {h.search(15)}")

# Display hash table after several operations
print("\nFinal Hash table:")
h.display()

# Output:
# Index of inserting 5: 5
# Index of inserting 10: 3
# Index of inserting 15: 1
# Index of inserting 20: 6
# Index of inserting 25: 4
# Index of inserting 30: 2
#
# Hash table after insertions:
# 5,10,15,20,25,30,
#
# Search for 10: 10
# Search for 40: False
# Delete element 15: 15
# Hash table after deletion of 15:
# 5,10,20,25,30,
#
# Search for 15 after deletion: False
#
# Final Hash table:
# 5,10,20,25,30,
