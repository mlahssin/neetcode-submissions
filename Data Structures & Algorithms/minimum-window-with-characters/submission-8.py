class Solution:


    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s) or not t:
            return ""


        t_hash = {}

        for c in t:
            t_hash[c] = t_hash.get(c, 0) + 1

        res = ""

        have = 0

        need = len(t_hash)
        left = 0


        window_hash = {}
    
        
        for right in range(len(s)):
            c = s[right]

            window_hash[c] = window_hash.get(c, 0) + 1

            if c in t_hash and window_hash[c] == t_hash[c]:
                have += 1

            while have == need:

                txt = s[left: right + 1]

                if not res or len(txt) < len(res):
                    res = txt

                c = s[left]
                window_hash[c] -= 1

                if c in t_hash and window_hash[c] < t_hash[c]:
                    have -= 1
                left += 1
        return res



print(Solution().minWindow("OUZODYXAZV", "XYZ"))

        









