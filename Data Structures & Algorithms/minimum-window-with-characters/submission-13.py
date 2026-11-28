# class Solution:


#     def minWindow(self, s: str, t: str) -> str:
#         if len(t) > len(s) or not t:
#             return ""


#         t_hash = {}

#         for c in t:
#             t_hash[c] = t_hash.get(c, 0) + 1

#         res = ""

#         have = 0

#         need = len(t_hash)
#         left = 0


#         window_hash = {}
    
        
#         for right in range(len(s)):
#             c = s[right]

#             window_hash[c] = window_hash.get(c, 0) + 1

#             if c in t_hash and window_hash[c] == t_hash[c]:
#                 have += 1

#             while have == need:

#                 txt = s[left: right + 1]

#                 if not res or len(txt) < len(res):
#                     res = txt

#                 c = s[left]
#                 window_hash[c] -= 1

#                 if c in t_hash and window_hash[c] < t_hash[c]:
#                     have -= 1
#                 left += 1
#         return res



# print(Solution().minWindow("OUZODYXAZV", "XYZ"))


















class Solution:


    def minWindow(self, s: str, t: str) -> str:

        if len(t) > len(s):
            return ""

        hash_t = {}

        for c in t:

            hash_t[c] = hash_t.get(c, 0) + 1
        
        l, r = 0, 0

        hash_s = {}

        need = len(hash_t)
        
        have = 0

        res = ""

        while r < len(s):
            
            c = s[r]

            hash_s[c] = hash_s.get(c, 0) + 1


            if c in hash_t and hash_s[c] == hash_t[c]:
                have += 1

            
            while have == need:

                txt = s[l : r + 1]

                if not res or len(txt) < len(res):
                    res = txt
   
                
                
                left = s[l]

                hash_s[left] -= 1

                

                if left in hash_t and hash_s[left] < hash_t[left]:
                    have -= 1


                l += 1
            r += 1

        return res
                

                

            

                
            

            

        




























        









