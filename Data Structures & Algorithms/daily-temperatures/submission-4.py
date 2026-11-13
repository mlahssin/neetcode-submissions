from collections import deque

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> Ltemperatures:
        res = [0] * len(temperatures)
        dq = deque()

        for index, t in enumerate(temperatures):

            while dq and dq[-1][0] < t:
                elt = dq.pop()

                res[elt[1]] = index - elt[1]
            
            dq.append((t, index))

        return res
            

            




        
        


        