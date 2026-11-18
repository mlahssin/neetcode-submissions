class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:


        p = 1

        n = len(nums)

        if n == 0:
            return []

        prefix = [1] * n


        for i in range(n):

            prefix[i] *= p
            p *= nums[i]
        
        s = 1

        suffix = [1] * n

        for j in range(n - 1, -1 , -1):

            suffix[j] *= s

            s *= nums[j]

        res = [1] * n



        for k in range(n):

            res[k] = prefix[k] * suffix[k]
        
        return res
        