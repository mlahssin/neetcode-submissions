from collections import deque

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        hash_set = set()

        n = len(s)

        l = 0
        max_sub = 0

        for r in range(n):

            if s[r] in hash_set:

                while s[r] in hash_set:

                    hash_set.remove(s[l])

                    l += 1
            
            hash_set.add(s[r])

            max_sub = max(max_sub, r - l + 1)
        
        return max_sub








        