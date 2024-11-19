def is_balanced(s):
    stack = []
    matching = {')': '(', ']': '[', '}': '{'}
    
    for char in s:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if not stack or stack[-1] != matching[char]:
                return "The input string is NOT balanced."
            stack.pop()
    
    return "The input string is balanced." if not stack else "The input string is NOT balanced."

# Example Usage
s = input("Enter a string of parentheses: ")
print(is_balanced(s))
