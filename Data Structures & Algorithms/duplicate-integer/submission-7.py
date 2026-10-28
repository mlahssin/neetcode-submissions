class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        checks = set()

        for item in nums:
            if item in checks:
                return True
            checks.add(item)
        return False
        


        