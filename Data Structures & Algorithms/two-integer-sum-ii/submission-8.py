class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hash_map = {}

        for index, n in enumerate(numbers):

            rest = target - n

            if n in hash_map:
                return [hash_map[n], index + 1]
            else:
                hash_map[rest] = index + 1
        
        return []
        