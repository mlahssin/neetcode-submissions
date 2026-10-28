


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


            
        


        
        