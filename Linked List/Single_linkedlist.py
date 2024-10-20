class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.ref = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
    
    # Add an element at the beginning of the linked list
    def add_begin(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node
        
    # Add an element at the end of the linked list
    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node
            
    # Add an element after a specific node
    def add_after(self, data, x):
        n = self.head
        while n is not None:
            if x == n.data:
                break
            n = n.ref
        if n is None:
            print('Node is not present in LL')
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node
            
    # Add an element before a specific node
    def add_before(self, data, x):
        if self.head is None:
            print("Linked List is empty!")
            return
        if self.head.data == x:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
            return
        n = self.head
        while n.ref is not None:
            if n.ref.data == x:
                break
            n = n.ref
        if n.ref is None:
            print("Node is not found!")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node
            
    # Insert an element in an empty linked list
    def insert_empty(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print('Linked list is not empty')
            
    # Delete an element at the beginning of the linked list
    def delete_begin(self):
        if self.head is None:
            print('Cannot delete, the list is empty')
        else:
            self.head = self.head.ref
        
    # Delete an element at the end of the linked list
    def delete_end(self):
        if self.head is None:
            print('The list is empty')
        elif self.head.ref is None:
            self.head = None
        else:
            n = self.head
            while n.ref.ref is not None:
                n = n.ref
            n.ref = None
            
    # Delete an element by its value
    def delete_by_value(self, x):
        if self.head is None:
            print('Cannot delete, the list is empty')
            return
        
        if x == self.head.data:
            self.head = self.head.ref
            return
        n = self.head
        while n.ref is not None:
            if x == n.ref.data:
                break
            n = n.ref
            
        if n.ref is None:
            print('Node is not present')
        else:
            n.ref = n.ref.ref
            
    # Search for an element by its value
    def search(self, value):
        if self.head is None:
            print("Linked list is empty.")
            return
        
        n = self.head
        while n is not None:
            if n.data == value:
                print(f"Element {value} found in the linked list.")
                return
            n = n.ref
        
        print(f"Element {value} not found in the linked list.")
        
    # Find the length of the linked list
    def find_length(self):
        count = 0
        n = self.head
        while n is not None:
            count += 1
            n = n.ref
        print(f"Length of the singly linked list is: {count}")
        return count
    
    # Reverse the linked list
    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next = current.ref  # Save the next node
            current.ref = prev  # Reverse the link
            prev = current  # Move prev to this node
            current = next  # Move to the next node
        self.head = prev  # Update head to the last node
        print("Singly linked list reversed.")
        
    # Delete an element at a specific position
    def delete_at_position(self, position):
        if self.head is None:
            print("The linked list is empty.")
            return

        if position == 0:  # If position is 0 (head)
            self.head = self.head.ref
            return

        n = self.head
        for i in range(position - 1):  # Traverse to the node just before the desired position
            if n.ref is None:
                print("Position out of bounds.")
                return
            n = n.ref

        if n.ref is None:
            print("Position out of bounds.")
            return

        n.ref = n.ref.ref  # Remove the node by adjusting the ref
        print(f"Node at position {position} deleted.")
        
    # Find the middle element of the linked list
    def find_middle_singly(self):
        if self.head is None:
            return None

        slow = self.head
        fast = self.head

        while fast is not None and fast.ref is not None:
            slow = slow.ref
            fast = fast.ref.ref

        return slow.data
    
    # Delete the middle element of the linked list
    def delete_middle_singly(self):
        if self.head is None:
            print("The linked list is empty.")
            return

        if self.head.ref is None:  # If there is only one element
            self.head = None
            return

        slow = self.head
        fast = self.head
        prev = None

        while fast is not None and fast.ref is not None:  # Using slow and fast pointer technique to find the middle
            prev = slow
            slow = slow.ref
            fast = fast.ref.ref

        if prev is not None:  # 'slow' is the middle node, 'prev' is the node before it
            prev.ref = slow.ref
        print(f"Middle node with value {slow.data} deleted.")

    # Check if the linked list is circular
    def is_circular_singly(self):
        if self.head is None:
            return False

        slow = self.head
        fast = self.head

        while fast is not None and fast.ref is not None:
            slow = slow.ref           # Move slow pointer by 1
            fast = fast.ref.ref      # Move fast pointer by 2

            if slow == fast:         # If they meet, there's a cycle
                return True

        return False  # No cycle found
    
    # Delete duplicate elements from the linked list
    def delete_duplicates(self):
        if self.head is None:
            print("The linked list is empty.")
            return

        n = self.head
        while n.ref is not None:
            if n.data == n.ref.data:  # Duplicate found
                n.ref = n.ref.ref  # Skip the duplicate node
            else:
                n = n.ref  # Move to the next node

    # Print the linked list
    def printLL(self):
        if self.head is None:
            print('The list is empty')
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.ref
                
        
# Create a linked list and test the functions
LL1 = LinkedList()
LL1.add_begin(10)
LL1.add_end(100)
LL1.add_begin(20)
LL1.add_after(1, 10)
LL1.add_before(4, 1)
LL1.printLL()

# Output:
# 20
# 10
# 1
# 4
# 100
