class hash_tabla:
    def __init__(self, size):
        self.size = size  # Size of the hash table
        self.array = [None for i in range(self.size)]  # Initialize the table with None

    def hash_function(self, key):
        # Hash function to calculate the index based on the key
        h = 0
        for char in key:
            h = h + ord(char)  # Summing the ASCII values of the characters in the key
        return h % self.size  # Returning the index within the table size

    def insert(self, key, value):
        # Insert a key-value pair into the hash table
        index = self.hash_function(key)
        self.array[index] = (key, value)  # Storing the key-value pair at the calculated index

    def get(self, key):
        # Retrieve the value associated with the given key
        index = self.hash_function(key)
        return self.array[index]  # Return the value stored at the calculated index

    def delete(self, key):
        # Delete the key-value pair from the table
        index = self.hash_function(key)
        self.array[index] = None  # Set the position to None to indicate that it is empty

    def displey(self):
        # Display all elements in the hash table
        for i in range(len(self.array)):
            print(self.array[i])


# Test cases
h1 = hash_tabla(10)
h1.insert("name", "muhammed")
h1.insert("age", "12")
h1.insert("address", "kkm")

print('The hash table elements are:')
h1.displey()

# Get the value for the key "name"
p = h1.get("name")
print(f"the name is {p}")

# Delete the key "name"
h1.delete("name")

# Display the hash table after deletion
print("\nThe hash table elements after deletion of 'name':")
h1.displey()

# Output:
# The hash table elements are:
# [None, None, None, None, None, None, None, None, ('name', 'muhammed'), ('age', '12')]
# the name is ('name', 'muhammed')
# The hash table elements after deletion of 'name':
# [None, None, None, None, None, None, None, None, None, ('age', '12')]
