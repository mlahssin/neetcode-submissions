from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        n = len(nums)

        if n == 0:
            return -1

        left = 0

        right = n - 1 


        while left <= right:

            middle = (right + left) // 2



            if nums[middle] == target:
                return middle
            
            elif nums[middle] < target:

                left = middle + 1
            else:
                right = middle - 1



        return -1



print(Solution().search([-1,0,2,4,6,8], 3))