class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        

        n = len(nums)

        if n == 0:
            return False
        
        checks = {}
        for item in nums:
            if checks.get(item) is not None:
                return True
            checks[item] = 1
            # checks.append(item)
        return False
        
        


        