from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        n = len(nums)

        if n == 0 or k <= 0:
            return []

        index_re = [[] for i in range(n + 1)]

        hash_map = {}
            
        for n in nums:
            if n not in hash_map:
                hash_map[n] = 1
            else:
                hash_map[n] += 1

        for key, value in hash_map.items():
            index_re[value].append(key)
        res = []

        for index in range(len(index_re) - 1, 0, -1):
            for i in index_re[index]:
                res.append(i)
                if len(res) == k:
                    return res
                
        