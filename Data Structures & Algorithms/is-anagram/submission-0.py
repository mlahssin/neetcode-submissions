class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        base1 = list(s)
        base2 = list(t)
        for elt in base1:
            if elt not in base2:
                return False
            base2.remove(elt)
        return True
