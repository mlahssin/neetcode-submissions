from collections import deque
from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        res = None

        dq = deque()
        res = 0


        for t in tokens:

            if t not in {'+', '-', '*', '/'}:
                dq.append(int(t))
            else:
                last = dq.pop()
                before_last = dq.pop()

                if t == '+':
                    res = last + before_last
                elif t == '-':
                    res = (before_last - last)
                elif t == '*':
                    res = (before_last * last)
                else:
                    res  = int(before_last / last)
                
                dq.append(res)
        return dq.pop()

            
print(Solution().evalRPN(["4","13","5","/","+"]))       