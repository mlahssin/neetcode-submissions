

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        hash_set_s = {}

        for item in s:
            if item not in hash_set_s:
                hash_set_s[item] = 1
            else:
                hash_set_s[item] += 1
        
        hash_set_t = {}

        for item in t:
            if item not in hash_set_t:
                hash_set_t[item] = 1
            else:
                hash_set_t[item] += 1
        

        return hash_set_s == hash_set_t
        