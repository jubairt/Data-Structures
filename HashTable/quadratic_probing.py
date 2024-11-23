class HashTable:
    def __init__(self, size):
        self.size = size  # Size of the hash table
        self.array = [None for i in range(self.size)]  # Initialize the table with None

    def hash_function(self, key):
        # Hash function to calculate the index based on the key
        h = 0
        for char in key:
            h += ord(char)  # Summing the ASCII values of the characters in the key
        return h % self.size  # Returning the index within the table size

    # Insert method with quadratic probing
    def insert(self, key, value):
        index = self.hash_function(key)  # Initial index based on the hash function
        i = 1  # Step for quadratic probing
        
        # Quadratic probing to find an empty slot
        while self.array[index] is not None:
            index = (self.hash_function(key) + i ** 2) % self.size  # Quadratic probing step
            i += 1  # Increment the step to explore the next index
        
        self.array[index] = (key, value)  # Insert the key-value pair at the found index

    # Get method with quadratic probing
    def get(self, key):
        index = self.hash_function(key)  # Initial index based on the hash function
        i = 1  # Step for quadratic probing
        
        # Quadratic probing to find the correct key
        while self.array[index] is not None:
            if self.array[index][0] == key:
                return self.array[index][1]  # Return the value if key matches
            index = (self.hash_function(key) + i ** 2) % self.size  # Quadratic probing step
            i += 1  # Increment the step to explore the next index
        return None  # Return None if key is not found

    # Delete method with quadratic probing
    def delete(self, key):
        index = self.hash_function(key)  # Initial index based on the hash function
        i = 1  # Step for quadratic probing
        
        # Quadratic probing to find the correct key
        while self.array[index] is not None:
            if self.array[index][0] == key:
                self.array[index] = None  # Delete the key-value pair
                return True
            index = (self.hash_function(key) + i ** 2) % self.size  # Quadratic probing step
            i += 1  # Increment the step to explore the next index
        return False  # Return False if key is not found to delete

    # Display the hash table elements
    def display(self):
        for i in range(len(self.array)):
            print(self.array[i])


# Example usage:
h1 = HashTable(10)  # Create a hash table with size 10
h1.insert("name", "muhammed")  # Insert key-value pair ("name", "muhammed")
h1.insert("age", "12")  # Insert key-value pair ("age", "12")
h1.insert("address", "kkm")  # Insert key-value pair ("address", "kkm")

print('The hash table elements are:')
h1.display()  # Display all elements in the hash table

p = h1.get("name")  # Get the value associated with the key "name"
print(f"The name is {p}")  # Print the value of "name"

h1.delete("name")  # Delete the key "name"
print("After deleting 'name':")
h1.display()  # Display the hash table after deleting "name"

# Expected Output:
# The hash table elements are:
# [None, None, None, None, None, None, ('address', 'kkm'), None, None, ('age', '12')]
# The name is muhammed
# After deleting 'name':
# [None, None, None, None, None, None, ('address', 'kkm'), None, None, ('age', '12')]
