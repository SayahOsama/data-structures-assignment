class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_symmetric(root):
    # Helper function to check mirror symmetry
    def is_mirror(t1, t2):
        if not t1 and not t2:
            return True
        if not t1 or not t2:
            return False
        return (t1.val == t2.val and 
                is_mirror(t1.left, t2.right) and 
                is_mirror(t1.right, t2.left))
    
    if not root:
        return True  # An empty tree is symmetric
    return is_mirror(root.left, root.right)

root = TreeNode(1)
root.left = TreeNode(2, TreeNode(3), None)
root.right = TreeNode(2, None, TreeNode(3))

print(is_symmetric(root))  # Output: True