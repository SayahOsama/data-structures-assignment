
def validate_parentheses(parentheses):
    matching_pairs = {')': '(', ']': '[', '}': '{'}
    stack = []
    
    for char in parentheses:
        if char in matching_pairs:
            if stack and stack[-1] == matching_pairs[char]:
                stack.pop()
            else:
                return False
        else:
            stack.append(char)
    
    return len(stack) == 0

balanced_parentheses = "([{}])"
print(validate_parentheses(balanced_parentheses))
unbalanced_parentheses = ")()[]"
print(validate_parentheses(unbalanced_parentheses))