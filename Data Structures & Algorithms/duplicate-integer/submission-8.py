# class Solution:
#     def hasDuplicate(self, nums: List[int]) -> bool:
        
#         checks = set()

#         for item in nums:
#             if item in checks:
#                 return True
#             checks.add(item)
#         return False
        





class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_set = set()

        for item in nums:

            if item in hash_set:
                return True
            hash_set.add(item)
        return False






































        