class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hash_map = {}

        for i , n in enumerate(nums):
            rest = target - n

            if rest in hash_map:
                return [hash_map[rest], i]
            hash_map[n] = i

        
        return []
            