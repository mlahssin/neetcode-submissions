class Solution:

    def productExceptSelf(self, nums: List[int]) -> List[int]:

        
        n = len(nums)

        res = [1] * n

        prefix = 1

        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]
        
        sufix = 1

        for i in range (n - 1, -1, -1):
            res [i] *= sufix
            sufix *= nums[i]
        
        return res
         # if n == 0:
        #     return []
        
        # start = [1] * n

        # prefix = None

        # for index, num in enumerate(nums):
        #     if prefix is None:
        #         start[index] = 1
        #         prefix = nums[index]
        #     else:
        #         start[index] = start[index - 1] * prefix
        #         prefix = nums[index]


        # index = n - 1

        # prefix = None

        # end = [1] * n

        # while index >= 0:
            
        #     if prefix is None:
        #         end[index] = 1
        #         prefix = nums[index]
        #     else:
        #         end[index] = prefix * end[index + 1]
        #         prefix = nums[index]
        #     index -= 1

        # res = []

        # index = 0

        # while index < n:
        #     res.append(start[index] * end[index])
        #     index += 1
        
        # return res
        

        