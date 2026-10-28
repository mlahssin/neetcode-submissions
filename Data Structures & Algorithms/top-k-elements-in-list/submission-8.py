
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
        
        heap = []
        for item in hash_set:
            heapq.heappush(heap, (hash_set[item], item))
        
        n = len(heap)

        while len(heap) > k:
            heapq.heappop(heap)
        
        heap = [x[1] for x in heap]
        
        return heap


            
        


Solution().topKFrequent([1,2,2,3,3,3], 2)
        
        