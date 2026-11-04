class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        n = len(nums)

        index = 0
        hash_map = {}

        res = []


        while index < n:

            j = index + 1
            k = n - 1

            while j < k:
                if nums[index] == -(nums[j] + nums[k]):
                    r = [nums[index], nums[j], nums[k]]
                    key = tuple(sorted(r))
                    if key not in hash_map:
                        hash_map[key] = r
                    j += 1
                    
                else:
                    if nums[index] +  nums[j] + nums[k] > 0:
                        k -= 1
                    else:
                        j += 1
            index += 1
            if index >= n or nums[index] > 0:
                break
            
            
        return list(hash_map.values())
             
