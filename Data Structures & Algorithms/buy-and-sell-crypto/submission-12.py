class Solution:
    def maxProfit(self, prices: List[int]) -> int:


        l , r = 0, 1

        max_P = 0

        while r < len(prices):

            if prices[r] > prices[l]:
                max_P = max(max_P, prices[r] - prices[l])
            else:
                l = r
            r += 1
        return max_P




        