class hash_table:
    def __init__(self, size):
        self.size = size
        self.array = [None for _ in range(self.size)]

    def hash_function(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        if self.array[index] is None:
            self.array[index] = (key, value)
            return
        next_index = (index + 1) % self.size
        while next_index != index:
            if self.array[next_index] is None:
                self.array[next_index] = (key, value)
                return
            next_index = (next_index + 1) % self.size
        print("The hash table is fully filled")

    def delete(self, key):
        for i in range(len(self.array)):
            if self.array[i] and self.array[i][0] == key:
                self.array[i] = None
                return
        print(f"Key '{key}' not found for deletion.")

    def display(self):
        for i in self.array:
            print(i)

    def get(self, key):
        for i in range(len(self.array)):
            if self.array[i] and self.array[i][0] == key:
                return self.array[i][1]
        return "The element is not present in the hash table"


# Test cases
l = hash_table(7)  # Create a hash table of size 7

# Insert keys and values
l.insert("apple", 100)
l.insert("banana", 200)
l.insert("grape", 300)
l.insert("melon", 400)
l.insert("peach", 500)

# Insert keys causing collisions
l.insert("cherry", 600)  # Linear probing resolves collision
l.insert("berry", 700)

# Try inserting into a full table
l.insert("plum", 800)  # This should print: The hash table is fully filled

# Delete a key
l.delete("banana")

# Display the hash table structure
print("Hash table after operations:")
l.display()
# Output:
# ('apple', 100)
# None
# ('grape', 300)
# ('melon', 400)
# ('peach', 500)
# ('cherry', 600)
# ('berry', 700)

# Retrieve values
print("\nValue for 'apple':", l.get("apple"))  # Output: 100
print("Value for 'banana':", l.get("banana"))  # Output: The element is not present in the hash table
print("Value for 'peach':", l.get("peach"))  # Output: 500
