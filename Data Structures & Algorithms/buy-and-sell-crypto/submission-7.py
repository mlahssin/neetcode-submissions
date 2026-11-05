
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:


        l, r = 0, 1

        Max_P = 0

        while r < len(prices):

            if prices[l] < prices[r]:
                Max_P = max(Max_P, prices[r] - prices[l])
            else:
                l = r
            r += 1
        return Max_P
        # n = len(prices)
        # if n == 0 or n == 1:
        #     return 0

        # left = 0
        # right = n - 1

        # m_left_index = left
        # M_right_index = right

        # m_left = prices[left]
        # M_right = prices[right]



        # while left < n and right >= 0:
        #     if prices[left] < m_left and left< M_right_index:
        #         m_left_index = left
        #         m_left = prices[left]
            
        #     if prices[right] > M_right and right > m_left_index:
        #         M_right_index = right
        #         M_right = prices[right]

            
        #     left += 1
        #     right -= 1
        
        # print(m_left)
        # print(M_right)
        # return max(M_right - m_left, 0)

print(Solution().maxProfit([5,1,5,6,7,1]))