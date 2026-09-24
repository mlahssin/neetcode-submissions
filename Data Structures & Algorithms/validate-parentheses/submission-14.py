class Solution:
    def isValid(self, text):
        pairs = {
            ')':'(',
            ']': '[',
            '}': '{'
        }
        stack = []
        for item in text:
            if item in "([{":
                stack.append(item)
            elif item in ")]}":
                if not stack or stack.pop() != pairs[item]:
                    return False
        return not stack
