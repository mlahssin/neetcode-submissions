class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        hash_s = [0] * 26
        for c in s:
            hash_s[ord(c) - ord('a')] += 1
        
        hash_t = [0] * 26

        for c in t:
            hash_t[ord(c) - ord('a')] += 1
        return hash_s == hash_t
