
def family_tree_search(tree, root, name):
    if root == name:
        return True
    for child in tree.get(root, []):
        if family_tree_search(tree, child, name):
            return True
    return False
    
    
family_tree = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": [],
    "F": []
}


# Test cases
print(family_tree_search(family_tree, "A", "E"))  # Output: True
print(family_tree_search(family_tree, "A", "Z"))  # Output: False