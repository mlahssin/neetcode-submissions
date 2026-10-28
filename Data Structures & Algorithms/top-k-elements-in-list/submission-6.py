import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_set = {}
        if not nums or k <= 0:
            return []

        for item in nums:
            if item not in hash_set:
                hash_set[item] = 1
            else:
                hash_set[item] += 1
        
        hash_set = dict(sorted(hash_set.items(),key=lambda x :
                 x[1],reverse=True))

        

        return list(hash_set.keys())[:k]

            
        


Solution().topKFrequent([1,2,2,3,3,3], 2)
        
        