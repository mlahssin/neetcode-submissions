class Solution:
    def trap(self, height: List[int]) -> int:

        n = len(height)

        index = 0

        max_prefix = [0] * n

        max_pr = 0

        for index, num in enumerate(height):
            max_prefix[index] = max_pr

            if num > max_pr:
                max_pr = num

        max_suff = 0

        max_suffix = [0] * n

        for index in range(n - 1, -1, -1):
            max_suffix[index] = max_suff

            if height[index] > max_suff:
                max_suff = height[index]
        water_trap = 0

        for index in range(n):
            w = min(max_prefix[index],
                max_suffix[index]) - height[index]
            if w > 0:
                water_trap += w

        return water_trap
        
        

        



        