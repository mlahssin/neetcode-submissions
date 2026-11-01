class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hash_map = {}

        for index , n in enumerate(nums):

            elt = target - n

            if n in hash_map:
                return [hash_map[n], index]
            else:
                hash_map[elt] = index
        return []
        