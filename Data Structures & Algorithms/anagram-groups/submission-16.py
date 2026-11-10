from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hash_map = defaultdict(list)

        for s in strs:

            alpha = [0] * 26

            for c in s:
                alpha[ord(c) - ord('a')] += 1
            
            hash_map[tuple(alpha)].append(s)
        
        return list(hash_map.values())

        