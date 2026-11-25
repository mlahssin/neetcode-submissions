class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        l , r = 0 , len(numbers) - 1


        while l <= r:

            res = numbers[l] + numbers[r] 
            if res == target:
                return [l + 1, r + 1]
            else:
                if res < target:
                    l += 1
                else:
                    r -= 1
        
        return []


