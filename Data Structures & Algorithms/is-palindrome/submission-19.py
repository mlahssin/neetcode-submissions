# class Solution:
#     def isPalindrome(self, s: str) -> bool:



#         new_s = "".join(c.lower() for c in s if c.isalnum())

#         return new_s == new_s[::-1]


class Solution:
    def isPalindrome(self, s: str) -> bool:

        n = len(s)

        left = 0
        right = n - 1

        while left < right:
            
            while left < n and not s[left].isalnum():
                left += 1
                if left == n:
                    return True

            while right >= 0 and not s[right].isalnum():
                right -= 1

                if right == 0:
                    return True
            
            if s[left].lower() != s[right].lower():
                return False
            
            right -= 1
            left += 1
            
        return True

            