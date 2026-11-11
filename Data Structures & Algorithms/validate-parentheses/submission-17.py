from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:

        my_dict = {
           '}' : '{' ,
           ')' : '(',
            ']':'['
        }
        dq = deque()

        for c in s:
            if c in my_dict.values():
                dq.append(c)
            else:
                if not dq:
                    return False
                elt = dq.pop()
                if elt != my_dict[c]:
                    return False
        if not dq:
            return True
        else:
            return False
