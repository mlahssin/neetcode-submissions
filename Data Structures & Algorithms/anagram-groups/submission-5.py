class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_set = {}

        for st in strs:
            hash_list = [0] * 26
            for c in st:
                index_c = ord(c) - ord('a')

                hash_list[index_c] += 1
            hash_str = tuple(hash_list)
            if hash_str not in hash_set:
                hash_set[hash_str] = [st]
            else:
                hash_set[hash_str].append(st)
        
        return [value for key, value in hash_set.items()]
