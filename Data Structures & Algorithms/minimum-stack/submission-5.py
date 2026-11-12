from collections import deque

class MinStack:

    def __init__(self):
        self.stack = deque()
        self.min = deque()
        self.prefix = None
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.prefix is None:
            self.min.append(val)
            self.prefix = val
        else:
            elt = min(self.prefix, val)
            self.prefix = elt
            self.min.append(elt)
        
        

    def pop(self) -> None:
        self.stack.pop()
        self.min.pop()
        if self.min:
            self.prefix = self.min[-1]
        else:
            self.prefix = None
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min[-1]

        
