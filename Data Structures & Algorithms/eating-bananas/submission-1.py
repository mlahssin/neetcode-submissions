from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        min_rate = 0

        left = 1

        right = max(piles)
        
        print(right)
        while left <= right:

            middle = (left + right) // 2

            print(middle)

            rate = 0

            for p in piles:

                if middle >= p:
                    rate += 1
                else:
                    
                    if p % middle == 0:
                        rate += p // middle
                    else:
                        rate += p // middle + 1
            

            if rate > h:
                left = middle + 1
            else:
                min_rate = middle
                right = middle - 1

        return min_rate            
        

print(Solution().minEatingSpeed([1,4,3,2], 9))
                    



        