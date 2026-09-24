class Solution:

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        for item in s:
            if item not in t:
                return False
            if s.count(item) != t.count(item):
                return False
            
        return True

        