class Node:
    def __init__(self, val) -> None:
        self.value = val
        self.left = None
        self.right = None


class Tree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, val):
        # Insert a new value using level order (breadth-first insertion)
        if not self.root:
            self.root = Node(val)
            return
        queue = [self.root]
        while queue:
            curr = queue.pop(0)
            # Insert in the left child if it's empty
            if curr.left is None:
                curr.left = Node(val)
                return
            else:
                queue.append(curr.left)
            # Insert in the right child if it's empty
            if curr.right is None:
                curr.right = Node(val)
                return
            else:
                queue.append(curr.right)

    def delete(self, val):
        # Delete a node with a given value using level order traversal
        if not self.root:
            return None
        node_delete = None
        queue = [self.root]
        while queue:
            curr = queue.pop(0)
            if curr.value == val:
                node_delete = curr  # Mark the node to be deleted
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        if not node_delete:
            return False  # Node not found
        node_delete.value = curr.value  # Replace the value of the node to delete with the last node's value
        self._delete_last(curr)  # Remove the last node

    def _delete_last(self, node):
        # Helper function to delete the last node (in level order)
        queue = [node]
        while queue:
            curr = queue.pop(0)
            if curr.left:
                if curr.left == node:
                    curr.left = None  # Remove left child
                else:
                    queue.append(curr.left)
            if curr.right:
                if curr.right == node:
                    curr.right = None  # Remove right child
                else:
                    queue.append(curr.right)

    def search(self, val):
        # Search for a value using level order traversal
        if not self.root:
            return False
        queue = [self.root]
        while queue:
            curr = queue.pop(0)
            if curr.value == val:
                return True
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        return False

    def find_depth(self, root, key, depth=0):
        # Find the depth of a key in the tree
        if root is None:
            return -1
        if root.value == key:
            return depth
        left_depth = self.find_depth(root.left, key, depth + 1)
        if left_depth != -1:
            return left_depth
        return self.find_depth(root.right, key, depth + 1)

    def height(self, node):
        # Find the height of the tree
        if node is None:
            return -1
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        return max(left_height, right_height) + 1

    def inorder(self, node):
        # Perform inorder traversal (left, root, right)
        if node is None:
            return
        self.inorder(node.left)
        print(node.value)
        self.inorder(node.right)

    def is_bst(self, node, min_val=float('-inf'), max_val=float('inf')):
        # Check if the tree is a binary search tree (BST)
        if node is None:
            return True
        if node.value <= min_val or node.value >= max_val:
            return False
        return (self.is_bst(node.left, min_val, node.value) and
                self.is_bst(node.right, node.value, max_val))


# Example usage
bt = Tree()
bt.insert(10)
bt.insert(5)
bt.insert(15)
bt.insert(2)
bt.insert(7)
bt.insert(12)
bt.insert(18)

print("Inorder Traversal:")
bt.inorder(bt.root)  # Expected Output: 2, 5, 7, 10, 12, 15, 18

print("Is the tree a BST?", bt.is_bst(bt.root))  # Should return True
