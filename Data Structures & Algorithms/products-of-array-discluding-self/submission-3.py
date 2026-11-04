from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)

        if n == 0:
            return []

        pre = 1 

        prefix = [1] * n
        print(type(prefix))

        for i in range(n):
            prefix[i] *= pre
            pre = prefix[i] * nums[i]
        
        
        suffix = [1] * n
        suff = 1

        for i in range(n - 1, -1, -1):
            suffix[i] *= suff
            suff = suffix[i] * nums[i]
        
        res = [1] * n
        for i in range(n):
            res[i] = suffix[i] * prefix[i]
        return res