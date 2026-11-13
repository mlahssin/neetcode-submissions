class Solution:
    def maxArea(self, heights: List[int]) -> int:

        l = 0

        r = len(heights) - 1

        Max_surface = 0

        while l < r:
            
            height = min(heights[l], heights[r])

            width = r - l

            Max_surface = max(Max_surface, height * width)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return Max_surface
    
        