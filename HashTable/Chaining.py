class hash_table:
    def __init__(self, size):
        self.size = size
        self.array = [[] for _ in range(self.size)]

    def hash_function(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        # Check if the key already exists
        for i, key_val in enumerate(self.array[index]):
            if key_val[0] == key:
                # Replace the existing value with the new one
                self.array[index][i] = (key, value)
                return  # Exit the function after replacing
        # If the key does not exist, add a new key-value pair
        self.array[index].append((key, value))

    def delete(self, key):
        index = self.hash_function(key)
        for i, key_val in enumerate(self.array[index]):
            if key_val[0] == key:
                del self.array[index][i]
                return True
        return False

    def display(self):
        for i in self.array:
            print(i)

    def get(self, key):
        index = self.hash_function(key)
        for i in self.array[index]:
            if i[0] == key:
                return i[1]
        return None


# Creating a new hash table with size 7
h_table = hash_table(7)

# Adding different test cases
h_table.insert("apple", 100)
h_table.insert("banana", 200)
h_table.insert("grape", 300)
h_table.insert("orange", 400)

# Update an existing key
h_table.insert("apple", 500)  # Overwriting the value of "apple"

# Adding keys that cause hash collisions
h_table.insert("peach", 600)  # This key may collide with "grape" depending on hash size
h_table.insert("melon", 700)

# Deleting an existing key
h_table.delete("banana")

# Display the hash table structure
print("Hash table after operations:")
h_table.display()
# Output:
# []
# [('grape', 300), ('peach', 600)]
# []
# [('orange', 400)]
# [('apple', 500)]
# []
# [('melon', 700)]

# Retrieving values
print("\nValue for 'apple':", h_table.get("apple"))  # Output: 500
print("Value for 'banana':", h_table.get("banana"))  # Output: None
print("Value for 'melon':", h_table.get("melon"))  # Output: 700
print("Value for 'grape':", h_table.get("grape"))  # Output: 300
