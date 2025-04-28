class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root_value=None):
        if root_value is not None:
            self.root = Node(root_value)
        else:
            self.root = None
        # Removed the print statement here

    def height(self):
        def _height(node):
            if not node:
                return 0
            return 1 + max(_height(node.left), _height(node.right))
        return _height(self.root)

    def size(self):
        def _size(node):
            if not node:
                return 0
            return 1 + _size(node.left) + _size(node.right)
        return _size(self.root)

    def count_leaves(self):
        def _count_leaves(node):
            if not node:
                return 0
            if not node.left and not node.right:
                return 1
            return _count_leaves(node.left) + _count_leaves(node.right)
        return _count_leaves(self.root)

    def is_full_binary_tree(self):
        def _is_full(node):
            if not node:
                return True
            if (node.left is None) and (node.right is None):
                return True
            if node.left and node.right:
                return _is_full(node.left) and _is_full(node.right)
            return False
        return _is_full(self.root)

    def is_complete_binary_tree(self):
        if not self.root:
            return True
        
        queue = [(self.root, 0)]
        i = 0
        while i < len(queue):
            node, idx = queue[i]
            i += 1
            if node:
                queue.append((node.left, 2 * idx + 1))
                queue.append((node.right, 2 * idx + 2))
        
        return queue[-1][1] == len(queue) - 1

# Create tree and add nodes manually
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

# Display information about the tree
print("Tree Height:", tree.height())
print("Total Nodes:", tree.size())
print("Leaf Nodes Count:", tree.count_leaves())
print("Is Full Binary Tree:", tree.is_full_binary_tree())
print("Is Complete Binary Tree:", tree.is_complete_binary_tree())
