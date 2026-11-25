from collections import deque

class Solution:
    def trap(self, height: List[int]) -> int:


        n = len(height)

        right = [0] * n

        left = [0] * n

        stack = deque()

        max_prefix = 0

        for h in range(len(height)):

            left[h] = max_prefix

            if height[h] > height[max_prefix]:
                max_prefix = h

        max_suffix = len(height) - 1

        for he in range(len(height) - 1, -1, -1):

            right[he] = max_suffix

            if height[he] > height[max_suffix]:
                max_suffix = he

        res = 0


        for i in range(len(height)):

            res += max(min(height[left[i]], height[right[i]]) - height[i], 0)


        return res

            
            




        
        

        
