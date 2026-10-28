
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hash_set = {}
        


        if not nums or k <= 0:
            return []

        n = len(nums)

        element_rep = [[] for i in range(n + 1)]
       
        for item in nums:
            if item not in hash_set:
                hash_set[item] = 1
            else:
                hash_set[item] += 1
    
        for key, value in hash_set.items():
            element_rep[value].append(key)
        
        res = []

        for index in range(len(element_rep) - 1, 0, -1):
            for i in element_rep[index]:
                res.append(i)
                if len(res) == k:
                    return res        
                
 
                

        
        # o(k) : k len(hash_set at worst case k would be n in case
        # all elts are distincts)

        # heap = []
        # # o(klogk)
        # for item in hash_set:
        #     # pushing to heap is o(logk) in worst case o(logn)
        #     heapq.heappush(heap, (hash_set[item], item))
        
        # n = len(heap)

        # # o(len(heap) - k) 
        # while len(heap) > k:
        #     heapq.heappop(heap)
        
        # #o(k)
        # heap = [x[1] for x in heap]
        # # complexity total could be o(k log k)
        # return heap



            
        


Solution().topKFrequent([1,2], 2)
        
        