class Node:
    def __init__(self, val) -> None:
        self.value = val  # The value of the node
        self.left = None   # Pointer to left child
        self.right = None  # Pointer to right child


class BST:
    def __init__(self) -> None:
        self.root = None  # Initially, the tree is empty

    def insert(self, val):
        if self.root is None:
            self.root = Node(val)  # If the tree is empty, insert the root node
            return
        self._insert_recur(self.root, val)  # Otherwise, insert recursively

    def _insert_recur(self, node, val):
        if val < node.value:
            if node.left is None:
                node.left = Node(val)  # Insert on the left if value is smaller
            else:
                self._insert_recur(node.left, val)  # Recursively insert on the left
        elif val > node.value:
            if node.right is None:
                node.right = Node(val)  # Insert on the right if value is greater
            else:
                self._insert_recur(node.right, val)  # Recursively insert on the right
        else:
            return  # If value already exists, do nothing

    def delete(self, key, node):
        if self.root is None:
            return None  # Return None if the tree is empty
        while node:
            if key < node.value:
                node.left = self.delete(key, node.left)  # Recurse to the left
            elif key > node.value:
                node.right = self.delete(key, node.right)  # Recurse to the right
            else:
                # Node with the key found
                if node.left is None:
                    return node.right  # If no left child, return right child
                if node.right is None:
                    return node.left  # If no right child, return left child
                # Node has two children, replace with the minimum node from right subtree
                temp = self.find_min(node.right)
                node.value = temp.value
                node.right = self.delete(temp.value, node.right)  # Delete the duplicate
            return node  # Return the modified node

    def find_min(self, node):
        if node is None:
            return None  # Return None if the node is empty
        current = node
        while current.left:
            current = current.left  # Find the leftmost node (minimum value)
        return current

    def search(self, key):
        def _search(node, key):
            if node is None:
                return False  # Return False if key is not found
            if node.value == key:
                return True  # Return True if key matches node value
            elif key < node.value:
                return _search(node.left, key)  # Search in the left subtree
            else:
                return _search(node.right, key)  # Search in the right subtree
        if self.root is None:
            return False  # If tree is empty, return False
        return _search(self.root, key)  # Start search from root

    def sum_of_nodes(self):
        return self._sum_nodes_rc(self.root)  # Start recursive summation from root

    def _sum_nodes_rc(self, node):
        if node is None:
            return 0  # If node is empty, return 0
        return (node.value + self._sum_nodes_rc(node.left) + self._sum_nodes_rc(node.right))  # Sum node value and recurse

    def findclosetnode(self, target):
        return self.findcloset_rc(self.root, target)  # Start recursive search for closest node

    def findcloset_rc(self, node, target, closet=None):
        if node is None:
            return closet  # Return the closest node value found so far
        if closet is None:
            closet = node.value  # Initialize closet if it’s the first node
        if abs(node.value - target) < abs(closet - target):
            closet = node.value  # Update closet if the current node is closer
        if target < node.value:
            return self.findcloset_rc(node.left, target, closet)  # Recurse left if target is smaller
        else:
            return self.findcloset_rc(node.right, target, closet)  # Recurse right if target is larger
        
    def postorder(self, node):
        if node is None:
            return
        self.postorder(node.left)  # Traverse left subtree
        self.postorder(node.right)  # Traverse right subtree
        print(node.value)  # Print the node value (postorder)

    def inorder(self, node):
        if node is None:
            return
        self.inorder(node.left)  # Traverse left subtree
        print(node.value)  # Print the node value (inorder)
        self.inorder(node.right)  # Traverse right subtree

    def preorder(self, node):
        if node is None:
            return
        print(node.value)  # Print the node value (preorder)
        self.preorder(node.left)  # Traverse left subtree
        self.preorder(node.right)  # Traverse right subtree

    def height(self, node):
        if node is None:
            return -1  # Return -1 for null node
        left = self.height(node.left)  # Get height of left subtree
        right = self.height(node.right)  # Get height of right subtree
        return max(left, right) + 1  # Return the max height

    def depth(self, root, key, depth=0):
        if root is None:
            return -1  # Return -1 if node is not found
        if root.value == key:
            return depth  # Return the current depth if the key is found
        left = self.depth(root.left, key, depth + 1)  # Search left subtree
        if left != -1:
            return left  # If found in left subtree, return the depth
        return self.depth(root.right, key, depth + 1)  # Search right subtree

    def is_bst(self, node, min_val=float('-inf'), max_val=float('inf')):
        if node is None:
            return True  # An empty tree is a valid BST
        if node.value <= min_val or node.value >= max_val:
            return False  # If node value is out of bounds, it's not a BST
        # Recursively check the left and right subtrees
        return (self.is_bst(node.left, min_val, node.value) and
                self.is_bst(node.right, node.value, max_val))


# Example usage
tree = BST()
tree.insert(10)
tree.insert(20)
tree.insert(0)
tree.insert(100)
tree.inorder(tree.root)  # 0, 10, 20, 100
print(tree.search(20))  # True
print(tree.sum_of_nodes())  # 130
print(tree.findclosetnode(15))  # 10
print(tree.depth(tree.root, 100))  # 2
print(tree.height(tree.root))  # 3
