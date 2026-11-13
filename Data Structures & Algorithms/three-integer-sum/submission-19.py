class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        index = 0
        res = []

        while index < len(nums) - 2:
            left = index + 1
            right = len(nums) - 1
            while left < right:
                if nums[index] == -(nums[left] + nums[right]):
                    elt = [nums[index], nums[left], nums[right]]
                    if elt not in res:   
                        res.append(elt)
                    left += 1
                else:
                    if nums[index] + nums[left] + nums[right] < 0:
                        left += 1
                    else:
                        right -= 1
            index += 1
        return res
                









        