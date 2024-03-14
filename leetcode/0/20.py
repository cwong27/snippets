class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for paren in s:
            if paren == '(' or paren == '[' or paren == '{':
                stack.append(paren)
            elif paren == ')':
                if len(stack) == 0 or stack.pop() != '(':
                    return False
            elif paren == ']':
                if len(stack) == 0 or stack.pop() != '[':
                    return False
            elif paren == '}':
                if len(stack) == 0 or stack.pop() != '{':
                    return False
        if len(stack) == 0:
            return True
        else:
            return False