from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        if not nums or k <= 0 or k > len(nums):
            return []
        
        dq = deque()

        res = []
        for r in range(len(nums)):

            # remove the left indexs that are outside the working window

            while dq and dq[0] <= r - k:
                dq.popleft()
            
            while dq and nums[dq[-1]] <= nums[r]:
                dq.pop()
            
            dq.append(r)

            if r >= k - 1:
                res.append(nums[dq[0]])
        
        return res


        # index = 0

        # n = len(nums)

        # res = []

        # while index + k - 1 < n:
        #     res.append(max(nums[index: index + k]))
        #     index += 1
        # return res    



                 