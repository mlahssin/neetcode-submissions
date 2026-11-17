
class Solution:
    def findMin(self, nums: List[int]) -> int:

        left = 0
        right = len(nums) - 1


        min_elt = nums[0]

        while left <= right:
            middle = (left + right) // 2

            if nums[middle] < min_elt:
                min_elt = nums[middle]
                right = middle - 1

            elif nums[middle] >= min_elt:
                left = middle + 1
    
        return min_elt
