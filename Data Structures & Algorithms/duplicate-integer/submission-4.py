class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        n = len(nums)

        if n == 0:
            return False
        
        checks = []

        for item in nums:
            if item in checks:
                return True
            checks.append(item)
        return False
        
        


        