from typing import List

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)

        
        left = 0
        right = n - 1
        MaxSurface = 0

        while left < right:
            height = min(heights[left], heights[right])


            width = right - left
    

            new_surface = height * width
            

            MaxSurface = max(MaxSurface, new_surface)
            

            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        
        return MaxSurface
    




print("res", Solution().maxArea([1,7,2,5,4,7,3,6]))


        