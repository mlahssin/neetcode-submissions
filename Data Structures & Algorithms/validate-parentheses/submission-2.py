class Solution:
    def isValid(self, s: str) -> bool:
        pair = {")": "(", "]": "[", "}": "{"}
        stack = []
        for c in s:
            if c in pair.values():
                stack.append(c)
            elif c in pair.keys():
                if not stack or stack[-1] != pair[c]:
                    return False
                stack.pop()
            else:
                return False
        return not stack
 
                
