class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = "".join(c.lower() for c in s if c.isalnum())
        i = 0
        j = len(clean) - 1
        if len(s) == 1:
            return True
        while i < len(clean):
            if clean[i] != clean[j]:
                return False
            i = i + 1
            j = j - 1
        return True
        