from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_set = defaultdict(list)

        for st in strs:
            hash_list = [0] * 26
            for c in st:
                index_c = ord(c) - ord('a')

                hash_list[index_c] += 1

            hash_str = tuple(hash_list)
            
            hash_set[hash_str].append(st)
        
        return list(hash_set.values())