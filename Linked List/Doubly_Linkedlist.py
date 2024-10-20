class Node:
    # Initialize a doubly linked list node
    def __init__(self, data) -> None:
        self.data = data
        self.nref = None  # Next reference
        self.pref = None  # Previous reference


class DoublyLL:
    # Initialize an empty doubly linked list
    def __init__(self) -> None:
        self.head = None

    # Insert a node in an empty list
    def insert_empty(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print('Linked list is not empty')

    # Add a node at the beginning
    def add_begin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.nref = self.head
            self.head.pref = new_node
            self.head = new_node

    # Add a node at the end
    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            n.nref = new_node
            new_node.pref = n

    # Add a node after a given node 'x'
    def add_after(self, data, x):
        n = self.head
        while n is not None:
            if x == n.data:
                break
            n = n.nref
        if n is None:
            print('Given node is not present in DLL')
        else:
            new_node = Node(data)
            new_node.nref = n.nref
            new_node.pref = n
            if n.nref is not None:
                n.nref.pref = new_node
            n.nref = new_node

    # Add a node before a given node 'x'
    def add_before(self, data, x):
        if self.head is None:
            print('LL is empty')
        else:
            n = self.head
            while n is not None:
                if x == n.data:
                    break
                n = n.nref
            if n is None:
                print('Given node is not present in DLL')
            else:
                new_node = Node(data)
                new_node.nref = n
                new_node.pref = n.pref
                if n.pref is not None:
                    n.pref.nref = new_node
                else:
                    self.head = new_node
                n.pref = new_node

    # Delete the first node
    def delete_begin(self):
        if self.head is None:
            print('LL is empty')
            return
        if self.head.nref is None:
            self.head = None
            print('LL is empty after deleting the node')
        else:
            self.head = self.head.nref
            self.head.pref = None

    # Delete the last node
    def delete_end(self):
        if self.head is None:
            print('DLL is empty')
            return
        if self.head.nref is None:
            self.head = None
            print('DLL is empty after deleting the node')
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            n.pref.nref = None

    # Delete a node by value
    def delete_by_value(self, x):
        if self.head is None:
            print('DLL is empty')
            return
        if self.head.nref is None:
            if x == self.head.data:
                self.head = None
            else:
                print('Value is not present in DLL')
            return
        if self.head.data == x:
            self.head = self.head.nref
            self.head.pref = None
            return
        n = self.head
        while n.nref is not None:
            if x == n.data:
                break
            n = n.nref
        if n.nref is not None:
            n.nref.pref = n.pref
            n.pref.nref = n.nref
        else:
            if n.data == x:
                n.pref.nref = None
            else:
                print('Value is not present in DLL')

    # Search for a value in the list
    def search(self, value):
        if self.head is None:
            print("Doubly linked list is empty.")
            return
        n = self.head
        while n is not None:
            if n.data == value:
                print(f"Element {value} found in the doubly linked list.")
                return
            n = n.nref
        print(f"Element {value} not found in the doubly linked list.")

    # Find the length of the doubly linked list
    def find_length(self):
        count = 0
        n = self.head
        while n is not None:
            count += 1
            n = n.nref
        print(f"Length of the doubly linked list is: {count}")
        return count

    # Reverse the doubly linked list
    def reverse(self):
        current = self.head
        last_node = None
        while current is not None:
            temp = current.nref
            current.nref = current.pref
            current.pref = temp
            last_node = current
            current = current.pref
        if last_node is not None:
            self.head = last_node
        print("Doubly linked list reversed.")

    # Delete a node at a specific position
    def delete_at_position(self, position):
        if self.head is None:
            print("The linked list is empty.")
            return
        if position == 0:
            self.head = self.head.nref
            if self.head is not None:
                self.head.pref = None
            return
        n = self.head
        for i in range(position - 1):
            if n.nref is None:
                print("Position out of bounds.")
                return
            n = n.nref
        if n.nref is None:
            print("Position out of bounds.")
            return
        n.nref = n.nref.nref
        if n.nref is not None:
            n.nref.pref = n
        print(f"Node at position {position} deleted.")

    # Find the middle element of the list
    def find_middle_doubly(self):
        if self.head is None:
            return None
        slow = self.head
        fast = self.head
        while fast is not None and fast.nref is not None:
            slow = slow.nref
            fast = fast.nref.nref
        return slow.data

    # Delete the middle element of the list
    def delete_middle_doubly(self):
        if self.head is None:
            print("The linked list is empty.")
            return
        if self.head.nref is None:
            self.head = None
            return
        slow = self.head
        fast = self.head
        while fast is not None and fast.nref is not None:
            slow = slow.nref
            fast = fast.nref.nref
        if slow.pref is not None:
            slow.pref.nref = slow.nref
        if slow.nref is not None:
            slow.nref.pref = slow.pref
        print(f"Middle node with value {slow.data} deleted.")

    # Check if the list is circular
    def is_circular_doubly(self):
        if self.head is None:
            return False
        slow = self.head
        fast = self.head
        while fast is not None and fast.nref is not None:
            slow = slow.nref
            fast = fast.nref.nref
            if slow == fast:
                return True
        return False

    # Delete duplicates in the doubly linked list
    def delete_duplicates(self):
        if self.head is None:
            print("The linked list is empty.")
            return
        n = self.head
        while n.nref is not None:
            if n.data == n.nref.data:
                duplicate_node = n.nref
                n.nref = duplicate_node.nref
                if duplicate_node.nref is not None:
                    duplicate_node.nref.pref = n
            else:
                n = n.nref

    # Forward traversing
    def printLL(self):
        if self.head is None:
            print('Linked list is empty')
        else:
            n = self.head
            while n is not None:
                print(n.data, end=" ")
                n = n.nref
            print()

    # Backward traversing
    def printLL_reverse(self):
        if self.head is None:
            print('Linked list is empty')
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            while n is not None:
                print(n.data, end=" ")
                n = n.pref
            print()

# Create a Doubly Linked List object
dll = DoublyLL()

# Perform operations on the doubly linked list
dll.add_end(10)
dll.add_end(20)
dll.add_end(30)
dll.add_begin(5)
dll.add_after(25, 20)
dll.add_before(15, 20)

# Print the list forward
dll.printLL()  # Output: 5 10 15 20 25 30

# Print the list backward
dll.printLL_reverse()  # Output: 30 25 20 15 10 5

# Search for an element
dll.search(25)  # Output: Element 25 found in the doubly linked list.

# Find the length of the list
dll.find_length()  # Output: Length of the doubly linked list is: 6

# Reverse the list
dll.reverse()  # Reverses the list

# Print the reversed list
dll.printLL()  # Output: 30 25 20 15 10 5

# Delete the middle node
dll.delete_middle_doubly()  # Output: Middle node with value 15 deleted.

# Print the list after deletion
dll.printLL()  # Output: 30 25 20 10 5
